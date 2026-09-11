- **QAM is unmapped on Ayaneo devices.** Use Home+A to open the Quick Access Menu.
- **White flash when initiating sleep and on boot-up.** This is a Retroid Pocket Nova-specific
  issue. Sleep flash occurs on S2idle only, does not affect sleep behavior otherwise.
- **Controls freeze when opening QAM.** Occurs in high GPU load scenarios. Toggling
  Vulkan Realtime Queue in **[Armada Control](./armada-control.md)** can alleviate the issue by allowing
  a half-summoned QAM to be dismissed with a second press of the QAM key.
- **"Resuming" window on wake freezes controls.** Usually resolves itself after a short time once
  the device has reconnected to the Internet following wake from sleep.
- **___ isn't working in Decky.** Due to Steam Client updates, Decky Loader often breaks. This
  can sometimes be resolved by reloading Decky in the crash screen, or reverting to **Steam Stable
  Client**. You may need to enable **Show Advanced Update Channels** in **Developer Settings**,
  then you will be able to change the **Steam Client Update Channel** from **Beta** to **Stable**.