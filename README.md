# NDS-HB-ABS (Homebrew Auto-Build System)

An automated system for creating and maintaining the ultimate MicroSD setup for Nintendo DS flashcarts.

## 🎯 Goal
Eliminate manual file management. This repository uses **GitHub Actions** to automatically download, configure, and package the latest versions of:
- **TWiLight Menu++** (Launcher)
- **nds-bootstrap** (Kernel/Loader)
- **Emulators** (NES, GB, GBC, SNES, GBA, etc.)
- **System Tools** (GodMode9i)

## ⚠️ Critical Requirement
For the flashcart to recognize the MicroSD, it **MUST** be formatted as:
- **File System:** FAT32
- **Partition Table:** MBR
- **Cluster Size:** 32KB (recommended)

## 🚀 How to get the setup
There is no need to run anything locally. Go to the **Releases** section of this repository and download the latest `.zip` file.
1. Extract the content to the root of your MicroSD.
2. Add your games to the `/roms/` folder.
3. Ready to play!

---
*Automatically updated monthly via GitHub Actions.*

## 🙏 Credits and Acknowledgments

This project is made possible thanks to the incredible work of the Nintendo DS homebrew community:

- **[DS-Homebrew](https://github.com/DS-Homebrew)**: For `TWiLight Menu++`, `nds-bootstrap`, and `GodMode9i`.
- **[LifehackerHansol](https://github.com/lifehackerhansol)**: For universal kernels and loaders.
- **Emulator Authors**: GameYob (D_S_O), nesDS (Loopy/Dwedit), SNEmulDS (Archeide), NitroGrafx (FluBBa), PicoDrive (Notaz/Irastussa), ColecoDS (Alekmaul).

Special thanks to **GBATemp** and the **DS-Homebrew Wiki** community for documentation and software preservation.
