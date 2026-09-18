import json
import re
from urllib import request, error

GITHUB_RELEASES_URL = "https://api.github.com/repos/armada-os/armada/releases"
DOWNLOAD_RE = re.compile(
    r"\[[^\]]*?(armada-\d{8}\.img(?:\.gz)?)[^\]]*\]\((https?://[^\s)]+)\)",
    re.IGNORECASE,
)
RAW_URL_RE = re.compile(
    r"https?://[^\s)]+/(?:release/)?(armada-\d{8}\.img(?:\.gz)?)(?:[?&#][^\s)]*)?",
    re.IGNORECASE,
)


def _fetch_json(url):
    req = request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "armada-docs-build",
        },
    )
    with request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def _extract_download(release):
    body = release.get("body") or ""
    match = DOWNLOAD_RE.search(body)
    if match:
        return {"name": match.group(1), "url": match.group(2)}

    match = RAW_URL_RE.search(body)
    if match:
        return {"name": match.group(1), "url": match.group(0)}

    return None


def _normalize_release_body(body):
    if not body:
        return body

    body = re.sub(r"\]\((?!https?://|mailto:|#)([^)]+)\)", lambda match: _normalize_link(match), body)

    lines = body.splitlines()
    normalized = []
    in_warning = False
    warning_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("> [!WARNING]"):
            in_warning = True
            warning_lines = ["!!! warning"]
            normalized.append("")
            continue

        if in_warning:
            if stripped.startswith(">"):
                text = stripped[1:].strip()
                if text:
                    warning_lines.append(f"    {text}")
                continue
            if not stripped:
                continue
            in_warning = False
            normalized.extend(warning_lines)
            normalized.append("")

        normalized.append(line)

    if in_warning:
        normalized.extend(warning_lines)

    return "\n".join(normalized).strip()


def _normalize_link(match):
    target = match.group(1)
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return match.group(0)
    normalized = target.strip()
    if normalized.startswith("/"):
        return match.group(0)
    return match.group(0).replace(f"({target})", f"(https://github.com/armada-os/armada/blob/main/{normalized})")


def _release_to_markdown(release):
    body = _normalize_release_body((release.get("body") or "").strip())
    if body:
        return body.rstrip() + "\n"
    title = release.get("name") or release.get("tag_name") or "Release"
    return f"## {title}\n"


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "downloads/index.md":
        return markdown

    try:
        releases = _fetch_json(GITHUB_RELEASES_URL)
    except (error.URLError, error.HTTPError, ValueError):
        return (
            markdown
            + "\n\n!!! warning\n\n"
            "    Unable to load release data from GitHub right now. Please check the GitHub releases page directly."
        )

    visible = [
        release
        for release in releases
        if not release.get("draft") and (release.get("body") or _extract_download(release))
    ]

    if not visible:
        return markdown + "\n\nNo published releases were found."

    latest, *archive = visible
    sections = [
        "# Downloads",
        "",
    ]

    sections.append(_release_to_markdown(latest))

    if archive:
        sections.extend([
            "",
            "## Archive",
            "",
        ])
        for release in archive:
            sections.extend([
                '<details markdown="1">',
                f"<summary>{release.get('name') or release.get('tag_name') or 'Release'}</summary>",
                "",
            ])
            sections.append(_release_to_markdown(release))
            sections.extend([
                "",
                "</details>",
                "",
            ])

    return "\n".join(sections)
