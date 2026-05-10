# NDS-HB-ABS (Homebrew Auto-Build System)

An automated system for creating and maintaining the ultimate MicroSD setup for Nintendo DS flashcarts.

## 🎯 Goal
Eliminate manual file management. This repository uses **GitHub Actions** to automatically download, configure, and package the latest versions of the best DS homebrew.

## ✨ Key Features
- **🚀 Timebomb Bypass:** Bypasses official kernel limitations and date-locks by booting directly into a modern homebrew environment using custom `R4.dat` and `BOOT.NDS` loaders.
- **📦 Automated Setup:** Automatically fetches and configures the latest versions of **TWiLight Menu++** and **nds-bootstrap**.
- **🔌 Plug & Play:** No local installation or Python knowledge required. Just download the latest release and copy it to your SD card.
- **🎮 All-in-One:** Comes with pre-configured emulators for NES, SNES, GB, GBC, Genesis, and more.

### 📊 Comparison: Manual vs. NDS-HB-ABS
| Feature | Manual Setup | **NDS-HB-ABS** |
| :--- | :--- | :--- |
| **Setup Time** | 15-30 mins | **< 1 min** |
| **Updates** | Manual search | **Always latest (Auto)** |
| **Timebomb** | Risks present | **Bypassed** |
| **Complexity**| High (Find Kernel) | **Zero (Just Copy)** |

## ⚠️ Critical Requirement
For the flashcart to recognize the MicroSD, it **MUST** be formatted as:
- **File System:** FAT32
- **Partition Table:** MBR
- **Cluster Size:** 32KB (recommended)

## 🚀 How to get the setup
1. Go to the **Releases** section of this repository and download the latest **`NDS-Homebrew-Setup.zip`**.
2. Extract the content to the root of your MicroSD.
3. Add your games to the `/roms/` folder.
4. **Ready to play!**

*Note: Developed and tested on modern R4i SDHC Gold Pro clones.*

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
- **GB/GBC:** [GameYob](https://github.com/DS-Homebrew/GameYob)
- **NES:** [nesDS](https://github.com/DS-Homebrew/nesDS)
- **SNES:** [SNEmulDS](https://github.com/cotodevel/SnemulDS)
- **Genesis:** [PicoDrive](https://github.com/DS-Homebrew/PicoDriveTWL)
- **Master System/GG:** [S8DS](https://github.com/FluBBaOfWard/S8DS)
- **ColecoVision:** [ColecoDS](https://github.com/wavemotion-dave/ColecoDS)
- **PC Engine:** [NitroGrafx](https://github.com/FluBBaOfWard/NitroGrafx)

Special thanks to **GBATemp** and the **DS-Homebrew Wiki** community for documentation and software preservation.
