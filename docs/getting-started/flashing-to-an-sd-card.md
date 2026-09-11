## Overview

Armada provides you the option to install entirely to a SD card.

Once it is running, you can optionally install it to internal storage so it boots without the card (see [Install to Internal Storage](./install-to-internal-storage.md)).

## Steps
1. Download `armada-YYYYMMDD.img.gz` from the latest [GitHub Release](https://github.com/armada-os/armada/releases/latest)

2. Flash the downloaded image to a 64GB or larger SD card (A2 speed for best results).

    !!! note

        Common flashing tools include [Balena Etcher](https://www.balena.io/etcher/), [Raspberry Pi Imager](https://www.raspberrypi.com/software/), and [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/). If you're skilled with the command line, `dd` works fine too.

3. Flash the ROCKNIX ABL for your device.

    - Insert the SD card, boot into Android, and copy the `rocknix_abl` folder to
      the root of your internal storage.

    - Identify your SoC from [Supported Devices](../devices/supported-devices.md) (`SM8550`, `SM8650`, or
      `SM8750`).

        !!! warning

            Flashing the wrong SoC's ABL can brick the device, so match it
            carefully.

    - Using your device's built-in "run script as root" tool, browse to your SoC's
      subfolder (e.g. `rocknix_abl/SM8550`) and run `backup_abl.sh`.

    - Copy the backup (`abl_a.img` and `abl_b.img`, written into your SoC subfolder)
      to your PC for safekeeping.

    - Run `flash_abl.sh` the same way to flash the new ABL.

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
