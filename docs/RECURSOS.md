# 📚 Proyectos y Recursos NDS / R4 — Referencia

> Recopilación de repositorios Git, homebrew, emuladores, kernels y recursos comunitarios
> para Nintendo DS con flashcarts R4.
>
> 📅 Última actualización: 2026-05-09

---

## 📋 Índice

- [Organización Principal](#-organización-principal-ds-homebrew)
- [Kernels y Firmware para R4](#-kernels-y-firmware-para-r4)
- [Launchers y Menús](#-launchers-y-menús)
- [Emuladores para NDS](#-emuladores-que-corren-en-nds)
- [Utilidades y Herramientas](#-utilidades-y-herramientas)
- [Juegos Homebrew](#-juegos-homebrew-open-source)
- [Multimedia](#-multimedia)
- [Desarrollo NDS](#-desarrollo--sdks)
- [Listas Curadas](#-listas-curadas--awesome-lists)
- [Emuladores de NDS (PC)](#-emuladores-de-nds-en-pc)
- [Comunidad y Wikis](#-comunidad-y-wikis)
- [ROM Hacks y Traducciones](#-rom-hacks-y-traducciones)
- [Notas Importantes](#-notas-importantes)

---

## 🏠 Organización Principal: DS-Homebrew

La organización central de la comunidad NDS homebrew en GitHub. **46 repositorios**, 539+ seguidores.

| Repo | Descripción | ⭐ | Lenguaje |
|------|------------|-----|----------|
| [TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu) | Menú reemplazo para DS/DSi/3DS/2DS | 3.9k | C++ |
| [nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap) | Bootea archivos .nds desde SD | 1.4k | C |
| [GodMode9i](https://github.com/DS-Homebrew/GodMode9i) | Explorador de archivos full-access | 633 | C |
| [SafeNANDManager](https://github.com/DS-Homebrew/SafeNANDManager) | Dump/restore DSi NAND | 51 | C |
| [twlmenu-extras](https://github.com/DS-Homebrew/twlmenu-extras) | Archivos extra para TWiLight Menu++ | 157 | Python |
| [DLDI](https://github.com/DS-Homebrew/DLDI) | Archivo de drivers DLDI para flashcards | 29 | C |
| [TWLHelper](https://github.com/DS-Homebrew/TWLHelper) | Bot de Discord DS⁽ⁱ⁾ Mode Hacking | 11 | Python |
| [wiki](https://github.com/DS-Homebrew/wiki) | Wikis para proyectos DS-Homebrew | 56 | HTML |
| [moonshell](https://github.com/DS-Homebrew/moonshell) | Reproductor multimedia clásico | — | — |

🔗 **Web oficial:** [ds-homebrew.com](https://ds-homebrew.com)
🔗 **Org GitHub:** [github.com/DS-Homebrew](https://github.com/DS-Homebrew)

---

## 🔧 Kernels y Firmware para R4

Esenciales para que la flashcart funcione correctamente. Si tu R4 tiene "time bomb", estos lo resuelven.

| Recurso | Descripción | Link |
|---------|------------|------|
| **Flashcard Archive** | Archivo de kernels oficiales y compatibles para MUCHAS flashcarts | [github.com/flashcarts/flashcard-archive](https://github.com/flashcarts/flashcard-archive) |
| **Flashcard Bootstrap** | Reemplazo moderno de kernel para flashcarts, lanza homebrew automáticamente | [github.com/lifehackerhansol/flashcard-bootstrap](https://github.com/lifehackerhansol/flashcard-bootstrap) |
| **YSMenu** | Firmware alternativo basado en DSTT, anti-timebomb | *(buscar en flashcard-archive)* |
| **Wood R4** | Firmware custom de alta compatibilidad y buena UI | *(buscar en flashcard-archive)* |
| **BL2CK** | Kernel comunitario para bypass de timebomb | *(buscar en GBAtemp)* |

### ⚠️ Tips de instalación:
1. **Identifica tu modelo exacto de R4** — Usar el kernel equivocado puede dejar la tarjeta inservible
2. **Formatear microSD en FAT32** (cluster 32KB para tarjetas viejas)
3. **Extraer archivos del kernel a la raíz** de la microSD
4. **Hacer backup** antes de cambiar firmware

---

## 🖥️ Launchers y Menús

| Proyecto | Descripción | Link |
|----------|------------|------|
| **TWiLight Menu++** | El launcher estándar moderno. Lanza DS, NES, SNES, GB, GBA ROMs y homebrew. Reemplaza el menú del DSi | [github.com/DS-Homebrew/TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu) |
| **nds-bootstrap** | Motor que permite cargar juegos NDS desde SD en DS/DSi/3DS | [github.com/DS-Homebrew/nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap) |

> **TWiLight Menu++ + nds-bootstrap** es la combinación gold standard para cualquier setup con R4 o CFW.

---

## 🎮 Emuladores que Corren EN NDS

Estos se ejecutan como archivos `.nds` en la flashcart:

### Consolas principales

| Consola | Emulador | Notas | Link/Fuente |
|---------|----------|-------|-------------|
| **GBA** | **GBARunner2** | No es emulador, es hypervisor — corre GBA nativo. Altísima compatibilidad | [github.com/Gericom/GBARunner2](https://github.com/Gericom/GBARunner2) |
| **GB / GBC** | **GameYob** | Recomendado sobre Lameboy, mejor compatibilidad | [github.com/Drenn1/GameYob](https://github.com/Drenn1/GameYob) |
| **GB / GBC** | **Lameboy DS** | Clásico pero superseded por GameYob | *(GameBrew)* |
| **NES** | **nesDS** | Emulador NES popular y estable | *(GameBrew)* |
| **SNES** | **SNEmulDS** | Rendimiento variable según el juego, puede requerir config | *(GameBrew)* |
| **Sega Genesis** | **jEnesisDS** | Recomendado por mejor rendimiento | *(GameBrew)* |
| **Sega Genesis** | **PicoDriveDS / PicoDriveTWL** | Alternativa si jEnesisDS tiene problemas de compat | *(GameBrew)* |
| **Point&Click** | **ScummVM DS** | Motor para juegos clásicos point-and-click (Monkey Island, etc.) | [github.com/scummvm/scummvm](https://github.com/scummvm/scummvm) |

### Notas de uso:
- Crear carpeta `Emulators/` en raíz de la microSD para los `.nds`
- Crear `ROMs/` con subcarpetas por sistema (`ROMs/GBA/`, `ROMs/SNES/`, etc.)
- GBARunner2 puede necesitar `bios.bin` (dump de BIOS de GBA)
- **DLDI patching** puede ser necesario en homebrew viejo (TWiLight Menu++ lo hace automáticamente)

---

## 🛠️ Utilidades y Herramientas

| Herramienta | Descripción | Link |
|------------|------------|------|
| **GodMode9i** | Explorador de archivos completo, manejo de saves, browse NAND | [github.com/DS-Homebrew/GodMode9i](https://github.com/DS-Homebrew/GodMode9i) |
| **SafeNANDManager** | Dump/restore de NAND DSi con nocash footer | [github.com/DS-Homebrew/SafeNANDManager](https://github.com/DS-Homebrew/SafeNANDManager) |
| **DiagnoSe** | Diagnóstico de hardware DS (pantallas, botones, etc.) | *(GameBrew)* |
| **nds-wifidump** | Dump de ROMs GBA y saves via WiFi | [github.com/Roman-Port/nds-wifidump](https://github.com/Roman-Port/nds-wifidump) |
| **DSload** | Transferir archivos de PC a DS via WiFi | [github.com/Lameguy64/dsload](https://github.com/Lameguy64/dsload) |
| **DLDI Archive** | Archivo de drivers DLDI para flashcards | [github.com/DS-Homebrew/DLDI](https://github.com/DS-Homebrew/DLDI) |

---

## 🕹️ Juegos Homebrew Open Source

### Juegos originales

| Juego | Descripción | Link |
|-------|------------|------|
| **AngunaDS** | RPG de acción/fantasía, muy popular | [github.com/asiekierka/AngunaDS](https://github.com/asiekierka/AngunaDS) |
| **Spelunky DS** | Port de Spelunky Classic | [github.com/dbeef/spelunky-ds](https://github.com/dbeef/spelunky-ds) |
| **DScraft** | Clon de Minecraft Classic para DS | [github.com/smealum/dscraft](https://github.com/smealum/dscraft) |
| **Space Impakto DS** | Bullet-hell shooter de alta calidad | [github.com/relminator/SpaceImpakto-DS](https://github.com/relminator/SpaceImpakto-DS) |
| **WordleDS** | Wordle para Nintendo DS | [github.com/Epicpkmn11/WordleDS](https://github.com/Epicpkmn11/WordleDS) |
| **WolveSlayer** | Hack-and-slash 3D | *(GameBrew)* |
| **PortalDS** | Adaptación de Portal de Valve | *(GameBrew)* |
| **Traffic Escape DS** | Puzzle 3D | *(GameBrew)* |
| **Meteora Galactic Battle** | Arcade espacial | *(GameBrew)* |
| **Pocket Physics** | Sandbox de física con touchscreen | *(GameBrew)* |

### Motores de juego

| Motor | Descripción | Link |
|-------|------------|------|
| **MegaZeux** | Motor de juegos text-mode-inspired para PC, portado a NDS | [github.com/AliceLR/megazeux](https://github.com/AliceLR/megazeux/tree/master/arch/nds) |
| **ScummVM** | Motor para aventuras point-and-click clásicas | [github.com/scummvm/scummvm](https://github.com/scummvm/scummvm) |

---

## 🎵 Multimedia

| App | Descripción | Link |
|-----|------------|------|
| **MoonShell** | Reproductor todo-en-uno: DPG video, MP3/OGG/MOD audio, imágenes, texto | [github.com/DS-Homebrew/moonshell](https://github.com/DS-Homebrew/moonshell) |
| **Colors!** | App de dibujo/pintura sofisticada con touchscreen | *(GameBrew)* |
| **tuna-viDS** | Reproductor de video XviD | [github.com/chishm/tuna-vids](https://github.com/chishm/tuna-vids) |
| **NitrousTracker** | Tracker de música compatible con DSi, fork mejorado de NitroTracker | [github.com/asiekierka/nitrotracker](https://github.com/asiekierka/nitrotracker/) |

---

## 💻 Desarrollo / SDKs

Para quien quiera **crear** homebrew para NDS:

| Recurso | Descripción | Link |
|---------|------------|------|
| **BlocksDS SDK** | SDK moderno, libre y open-source para NDS/DSi | [github.com/blocksds/sdk](https://github.com/blocksds/sdk) |
| **devkitARM** | Toolchain mantenido por devkitPro (el estándar clásico) | [devkitpro.org](https://devkitpro.org/) |
| **NDS-Homebrew-Development** | Repo con investigación y ejemplos para aprender a programar NDS | [github.com/jdriselvato/NDS-Homebrew-Development](https://github.com/jdriselvato/NDS-Homebrew-Development) |
| **Nitro Engine** | Wrapper alto nivel para el motor 3D: modelos, texturas, GUI, física | [github.com/AntonioND/nitro-engine](https://github.com/AntonioND/nitro-engine) |
| **NightFox's Lib** | Wrapper para tilemaps, sprites y collision maps (motor 2D) | [github.com/knightfox75/nds_nflib](https://github.com/knightfox75/nds_nflib) |
| **maxmod** | Motor de reproducción de audio .MOD/.S3M/.XM/.IT en ASM | [maxmod.devkitpro.org](https://maxmod.devkitpro.org/) |
| **libxm7** | Motor de reproducción .MOD/.XM | [github.com/blocksds/libxm7](https://github.com/blocksds/libxm7) |
| **dsmi** | Librería de interfaz MIDI | [github.com/asiekierka/dsmi](https://github.com/asiekierka/dsmi) |
| **dsi_sdmmc** | Driver custom de SDMMC para DSi | [github.com/profi200/dsi_sdmmc](https://github.com/profi200/dsi_sdmmc) |
| **uxnds** | Máquina virtual Varvara para NDS | [github.com/asiekierka/uxnds](https://github.com/asiekierka/uxnds) |

### Documentación técnica
- **[GBAtek](https://problemkaputt.de/gbatek.htm)** — LA referencia técnica para todo DS/DSi (~97% de lo que hay que saber)
  - [Versión paginada](https://problemkaputt.de/gbatek-contents.htm)
  - [Addendum/Errata](https://melonds.kuribo64.net/board/thread.php?id=13)
- **[Patater NDS Tutorial (2008)](https://www.patater.com/files/projects/manual/manual.html)** — Tutorial histórico crucial
- **[The History of DS Homebrew (2008)](https://web.archive.org/web/20081022153947/http://www.ndshb.com/modules.php?name=Content&pa=showpage&pid=40&page=1)** — Registro oral de los primeros años

---

## 📜 Listas Curadas / Awesome Lists

| Lista | Descripción | Link |
|-------|------------|------|
| **awesome-dsdev** | Lista curada de recursos para desarrollo NDS/DSi | [github.com/asiekierka/awesome-dsdev](https://github.com/asiekierka/awesome-dsdev) |
| **awesome-blocksds** | Software construido con BlocksDS | [codeberg.org/blocksds/awesome-blocksds](https://codeberg.org/blocksds/awesome-blocksds) |
| **Flashcard Archive** | Archivo completo de kernels para flashcarts | [github.com/flashcarts/flashcard-archive](https://github.com/flashcarts/flashcard-archive) |

---

## 🖥️ Emuladores de NDS en PC

Para testear y jugar en escritorio:

| Emulador | Descripción | Link |
|----------|------------|------|
| **melonDS** | Alta precisión, considerado el mejor actual | [melonds.kuribo64.net](https://melonds.kuribo64.net/) |
| **DeSmuME** | Clásico, muchas features de debug/dev | [desmume.org](https://desmume.org/) |
| **NO$GBA** | Emulador con herramientas de debugging avanzadas | [problemkaputt.de/gba.htm](https://problemkaputt.de/gba.htm) |
| **NooDS** | Emulador rápido y portátil, diseño ligero | *(GitHub)* |

---

## 🌐 Comunidad y Wikis

| Recurso | Descripción | Link |
|---------|------------|------|
| **DS-Homebrew Wiki** | Wiki oficial de la comunidad DS-Homebrew | [ds-homebrew.com](https://ds-homebrew.com/) |
| **GameBrew** | Wiki-database de TODO el homebrew NDS (apps, juegos, emuladores) | [gamebrew.org](https://www.gamebrew.org/) |
| **GBAtemp Forums** | El foro más activo para modding de consolas Nintendo | [gbatemp.net](https://gbatemp.net/) |
| **GBAdev Discord** | Discord de desarrollo GBA/NDS | [discord.io/gbadev](https://discord.io/gbadev) |
| **devkitPro Forums** | Soporte para toolchain devkitARM | [devkitpro.org/index.php](https://devkitpro.org/index.php) |
| **r/NintendoDS** | Subreddit de Nintendo DS | [reddit.com/r/NintendoDS](https://reddit.com/r/NintendoDS) |
| **dsi.cfw.guide** | Guía oficial para CFW en DSi | [dsi.cfw.guide](https://dsi.cfw.guide/) |
| **flashcarts.net** | Info sobre flashcarts y compatibilidad | [flashcarts.net](https://flashcarts.net/) |
| **r43ds.org** | Recurso de info sobre R4 | [r43ds.org](https://r43ds.org/) |

---

## 🔄 ROM Hacks y Traducciones

| Recurso | Descripción | Link |
|---------|------------|------|
| **Romhacking.net** | Archivo masivo de patches de traducción, hacks y utilidades | [romhacking.net](https://www.romhacking.net/) |
| **GameBrew (hacks)** | Sección de ROM hacks para NDS en GameBrew | [gamebrew.org](https://www.gamebrew.org/) |
| **xDelta / DeltaPatcher** | Herramientas para aplicar patches a ROMs | *(búsqueda directa)* |

---

## ⚠️ Notas Importantes

### WiFi en NDS
- El hardware DS **solo soporta WEP o redes sin contraseña**
- Para conectar, necesitas crear un hotspot inseguro o una red guest sin password

### DLDI Patching
- Homebrew viejo requiere "DLDI patching" para leer/escribir a la SD de la flashcart
- **TWiLight Menu++ lo hace automáticamente** — no te preocupes si usas esto

### Timebombs
- Muchos clones de R4 tienen fecha hardcodeada que bloquea la tarjeta
- **Solución:** Cambiar a YSMenu, Wood R4, o BL2CK (ver [Flashcard Archive](https://github.com/flashcarts/flashcard-archive))

### BIOS
- **GBARunner2** puede necesitar `bios.bin` (dump de BIOS GBA original)
- Algunos emuladores de GB también se benefician de BIOS dumps

### Estructura recomendada de microSD

```
📁 raíz microSD
├── 📁 _nds/              ← Archivos de TWiLight Menu++
├── 📁 Emulators/         ← Archivos .nds de emuladores
├── 📁 ROMs/
│   ├── 📁 NDS/
│   ├── 📁 GBA/
│   ├── 📁 SNES/
│   ├── 📁 NES/
│   ├── 📁 GB/
│   └── 📁 Genesis/
├── 📁 Homebrew/          ← Juegos y apps homebrew .nds
├── 📄 BOOT.nds           ← o archivo de boot del kernel
└── 📄 bios.bin           ← BIOS GBA (si se necesita)
```

---

## 🗂️ Quick Start — ¿Qué instalar primero?

1. **Kernel correcto** para tu modelo de R4 → [Flashcard Archive](https://github.com/flashcarts/flashcard-archive)
2. **TWiLight Menu++** → [GitHub](https://github.com/DS-Homebrew/TWiLightMenu)
3. **nds-bootstrap** → [GitHub](https://github.com/DS-Homebrew/nds-bootstrap)
4. **GodMode9i** → [GitHub](https://github.com/DS-Homebrew/GodMode9i)
5. **Emuladores que quieras** (GBARunner2, GameYob, nesDS, etc.)
6. Organizar ROMs y homebrew en carpetas

---

> 💡 **Para la lista más actualizada de TODAS las apps homebrew NDS:**
> → [gamebrew.org/wiki/List_of_DS_homebrew_applications](https://www.gamebrew.org/wiki/List_of_DS_homebrew_applications)
