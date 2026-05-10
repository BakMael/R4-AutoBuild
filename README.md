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

This project is built upon the incredible work of the Nintendo DS homebrew community:

### 🛠️ Core Components
- **Launcher:** [TWiLight Menu++](https://github.com/DS-Homebrew/TWiLightMenu)
- **Kernel/Loader:** [nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap)
- **System Tool:** [GodMode9i](https://github.com/DS-Homebrew/GodMode9i)
- **Custom Kernels:** [Universal Flashcard Loader](https://github.com/lifehackerhansol)

### 🕹️ Included Emulators
- **GB/GBC:** [GameYob](https://github.com/D-S-O/GameYob)
- **NES:** [nesDS](https://github.com/Arisotura/nesDS)
- **SNES:** [SNEmulDS](https://github.com/fiv0/SNEmulDS)
- **Genesis:** [PicoDrive](https://github.com/irastussa/PicoDriveTWL)
- **Master System/GG:** [S8DS](https://github.com/S8DS)
- **ColecoVision:** [ColecoDS](https://github.com/a-p-p-l-e-s/ColecoDS)
- **PC Engine:** [NitroGrafx](https://github.com/FluBBa/NitroGrafx)

Special thanks to **GBATemp** and the **DS-Homebrew Wiki** community for documentation and software preservation.
