// Add home page link to header title
document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector(".md-header__topic span.md-ellipsis");
    const logo = document.querySelector(".md-header__button.md-logo");
    if (!title || !logo)
    return;

    const homeHref = logo.getAttribute("href");
    if (!homeHref)
    return;

    const parent = title.parentElement;
    if (!parent || parent.tagName === "A")
    return;

    const titleLink = document.createElement("a");
    titleLink.setAttribute("href", homeHref);

    const logoTitle = logo.getAttribute("title");
    if (logoTitle)
    titleLink.setAttribute("title", logoTitle);

    parent.insertBefore(titleLink, title);
    titleLink.appendChild(title);
});
