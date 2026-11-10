## Overview

Armada provides you the option to install entirely to a SD card.

Once it is running, you can optionally install it to internal storage so it boots without the card (see [Install to Internal Storage](./install-to-internal-storage.md)).

## Steps
1. Download the latest `armada-YYYYMMDD.img.gz` from the [Downloads page](../../downloads/)

2. Flash the downloaded image to a 64GB or larger SD card (A2 speed for best results).

    !!! note

        Common flashing tools include [Balena Etcher](https://www.balena.io/etcher/), [Raspberry Pi Imager](https://www.raspberrypi.com/software/), and [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/). If you're skilled with the command line, `dd` works fine too.

3. Flash OpenABL for your device.

    - Insert the SD card, boot into Android, and copy the `openabl` folder to
      the root of your internal storage.

    - Identify your SoC from [Supported Devices](../devices/supported-devices.md) (`SM7750`, `SM8250`, `SM8550`, `SM8650`, or `SM8750`).

        !!! warning

            Flashing the wrong SoC's ABL can brick the device, so match it
            carefully.

    - Open **Android Settings** and find your device's built-in root script tool.
      On Retroid devices, the path is **Handheld Settings** > **Advanced** >
      **Run script as Root**.

        ![The Run script as Root option in Android's Handheld Settings on a Retroid Pocket Nova](../assets/images/getting-started/android-run-script-as-root.png){ width="600" }

        !!! note

            Menu names vary by manufacturer. Look in your device-specific settings
            for an option named **Run script as Root**, **Root Script**, or similar.

            *Thanks Bob*{ .root-script-easter-egg }

    - Choose the option to select a script, browse to your SoC's subfolder on
      internal storage (for example, `openabl/SM8550`), and select
      `backup_abl.sh`.

    - Copy the backup (`abl_a.img` and `abl_b.img`, written into your SoC subfolder)
      to your PC for safekeeping.

    - Return to the root script tool and select `flash_abl.sh` from the same
      subfolder to flash the new ABL.

4. Boot from SD and set your device model and boot mode.

    - Reboot holding your device's bootloader key to enter the ABL menu. For most
      devices, this is VOL-.

        !!! note "AYANEO Pocket DMG"

            Hold the `...` button above the volume wheel instead of VOL-. See the
            [AYANEO Pocket DMG device page](../devices/ayaneo/pocket-dmg.md) for
            device-specific notes.

    - In the ABL menu (navigate with VOL-/+, select with POWER):

        - Set your device model
        - Toggle boot mode to Linux
        - Choose Start to exit

        !!! warning "Retroid Pocket 5 and Pocket Flip 2 panel variants"

            Retroid has shipped these devices with two different display panels,
            with no reliable external way to tell them apart. Select the standard
            device model first. If Armada boots but the screen remains black,
            restart while holding VOL- and select the same model's **Visionox**
            entry instead. This changes the device tree used at boot and does not
            require flashing the ABL again.

5. Wait for Steam first-run setup.

    !!! note

        After the intro animation, the display may be black for up to 60 seconds
        before Steam appears. This is expected on the current SD card boot path.

    Eventually you will see Steam first-run where you can configure your
    language, timezone, and Wi-Fi. At the end Steam will restart again, and
    you may see another 60 seconds of black before the login screen appears.

Proceed to [Install to Internal Storage](./install-to-internal-storage.md) if you would like.

!!! note

    If you are an experienced user and know your way around Linux, you may want to try the bleeding-edge of features offered by Armada. Preview OS images are also available, which offer new features at the cost of system stability. See **[Preview Images](./preview-images.md)**.
