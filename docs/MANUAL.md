# 👑 NDS + R4 — Setup Definitivo 2026

> Documento consolidado final. Combina y mejora setup_1, setup_2 y proyectos_referencia.
> Incluye investigación nueva sobre GBARunner3, flashcard-bootstrap, FluBBa emulators y más.
>
> 📅 Compilado: 2026-05-09

---

## 📋 Índice

1. [Filosofía](#1--filosofía)
2. [Hardware y MicroSD](#2--hardware-y-microsd)
3. [Capa de Boot — Kernel R4](#3--capa-de-boot--kernel-r4)
4. [Core del Sistema](#4--core-del-sistema)
5. [Emulación Definitiva](#5--emulación-definitiva)
6. [Utilidades Esenciales](#6--utilidades-esenciales)
7. [Extras y QoL](#7--extras-y-qol)
8. [Multimedia](#8--multimedia-opcional)
9. [Estructura de Directorios](#9--estructura-de-directorios)
10. [Guía de Instalación Paso a Paso](#10--guía-de-instalación)
11. [Configuración Avanzada TWiLight](#11--configuración-avanzada-twilight)
12. [Mantenimiento y Backups](#12--mantenimiento-y-backups)
13. [Matriz por Consola](#13--matriz-por-consola)
14. [Qué NO Incluir](#14--qué-no-incluir)
15. [Resumen Final](#15--resumen-ejecutivo)

---

## 1. 🧠 Filosofía

```
La R4 es solo el puente físico.
El sistema real es TWiLight Menu++ + nds-bootstrap.
```

**Principios:**
- [x] Estructura de carpetas optimizada.
- [x] Configuración de TWiLight Menu++ y nds-bootstrap.
- [x] Autoboot configurado para R4i-SDHC (B6-V2.8).
- **Menos = mejor.** Solo lo esencial + lo que realmente uses
- **Híbrido:** Interfaz moderna (TWiLight) con fallback infalible (YSMenu)
- **ROMs limpias:** No-Intro, sin trim, sin patches manuales — nds-bootstrap parchea al vuelo
- **Backups primero:** `/saves/` es sagrado
- **No actualizar compulsivamente:** Si funciona, no tocar

---

## 2. 🛠️ Hardware y MicroSD

### MicroSD Recomendada

| Spec | Valor |
|------|-------|
| **Capacidad** | 32GB SDHC (ideal) / 64GB máx |
| **Clase** | Class 10 / U1 mínimo |
| **Marcas** | SanDisk, Samsung EVO, Kingston Canvas |
| **Tabla particiones** | **MBR** (R4 NO lee GPT) |
| **Formato** | **FAT32** |
| **Cluster** | **32KB** (≤32GB) / **64KB** (64GB) |

### Herramientas PC

| Herramienta | Uso | Link |
|-------------|-----|------|
| **GUIFormat** | Formatear FAT32 (Windows no lo hace >32GB) | [ridgecrop.co.uk](https://ridgecrop.co.uk/index.htm?guiformat.htm) |
| **SD Card Formatter** | Formato oficial SD Association | [sdcard.org](https://www.sdcard.org/downloads/formatter/) |
| **H2testw** | Verificar SD no es falsa / sectores corruptos | [heise.de](https://www.heise.de/download/product/h2testw-50539) |

> ⚠️ **SIEMPRE verificar SD nueva con H2testw antes de usarla**

---

## 3. 🔌 Capa de Boot — Kernel R4

### Opción A: flashcard-bootstrap (⭐ RECOMENDADO)

Reemplazo moderno de kernel. Simplemente bootea `BOOT.NDS` de la raíz.

- **Repo:** [github.com/lifehackerhansol/flashcard-bootstrap](https://github.com/lifehackerhansol/flashcard-bootstrap)
- **⭐** 53 stars, 14 releases, última v2.2.0
- **Soporta 20+ modelos de flashcart** incluyendo:
  - Original R4 (`_ds_menu.dat`)
  - DSTT (`ttmenu.dat`)
  - Acekard 2/2i (`akmenu4.nds`)
  - R4iDSN (`_dsmenu.dat`)
  - R4i-SDHC y clones con timebomb (`r4.dat`)
  - Ace3DS+, Gateway Blue, M3 DS Real, y más

**Ventaja:** Elimina timebombs, no necesitas YSMenu como kernel primario.

### Opción B: YSMenu / RetroGameFan (Fallback clásico)

- **Fuente:** [GBAtemp - RetroGameFan Updates](https://gbatemp.net/threads/retrogamefan-updates-releases.267243/)
- **Uso:** Fallback para clones problemáticos o juegos que nds-bootstrap no soporte

### Opción C: Kernel original del fabricante

- **Fuente:** [github.com/flashcarts/flashcard-archive](https://github.com/flashcarts/flashcard-archive)
- **Uso:** Solo si las otras opciones fallan con tu modelo específico

### Comparativa de opciones de boot

| Criterio | flashcard-bootstrap | YSMenu | Kernel original |
|----------|:------------------:|:------:|:--------------:|
| Anti-timebomb | ✅ | ✅ | ❌ |
| Mantenimiento activo | ✅ (2024) | ⚠️ Legacy | ❌ |
| Bootea TWiLight directo | ✅ | ⚠️ Config | ❌ |
| Modelos soportados | 20+ | 10+ | 1 |
| Complejidad | Baja | Media | Baja |

**Veredicto:** flashcard-bootstrap → TWiLight Menu++ como BOOT.NDS es el pipeline más limpio.

---

## 4. 🎛️ Core del Sistema

### Tier 0 — Absolutamente obligatorio

| Software | Función | Repo |
|----------|---------|------|
| **TWiLight Menu++** | Launcher universal, UI moderna, soporte themes/boxart | [DS-Homebrew/TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu) |
| **nds-bootstrap** | Motor que carga .nds desde SD, AP patch automático, widescreen | [DS-Homebrew/nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap) |

### Tier 1 — Altamente recomendado

| Software | Función | Repo |
|----------|---------|------|
| **GodMode9i** | Explorador archivos, dump cartuchos, manejo saves, browse NAND | [DS-Homebrew/GodMode9i](https://github.com/DS-Homebrew/GodMode9i) |
| **Universal-Updater** | App Store de DS — actualizar todo vía WiFi (activo, v3.3.3 ene 2026) | [Universal-Team/Universal-Updater](https://github.com/Universal-Team/Universal-Updater) |

> **Nota sobre Universal-Updater:** Requiere WiFi (WEP o sin password). Funciona en DSi/3DS con WiFi moderno. En DS/DS Lite es limitado por el hardware WiFi legacy.

---

## 5. 🎮 Emulación Definitiva

### Evaluación comparativa completa

| Sistema | Emulador Primario | Alternativa | Calidad | BIOS? | Notas |
|---------|:-:|:-:|:-:|:-:|------|
| **GBA** | **GBARunner2** | **GBARunner3** | ⭐⭐⭐⭐⭐ | Sí (`bios.bin`) | GBARunner2=estable, GBARunner3=experimental pero superior en títulos difíciles |
| **GB/GBC** | **GameYob** | Lameboy | ⭐⭐⭐⭐⭐ | No | Bordes SGB, paletas custom, save states |
| **NES** | **nesDS** | — | ⭐⭐⭐⭐ | No | Muy estable, builds en GitHub |
| **SNES** | **SNEmulDS** | — | ⭐⭐⭐ | No | Solo RPGs/platformers livianos. NO SuperFX/SA1 |
| **Genesis/MD** | **jEnesisDS** | PicoDriveTWL | ⭐⭐⭐⭐ | No | jEnesisDS mejor rendimiento general |
| **PC Engine** | **NitroGrafx** | — | ⭐⭐⭐⭐⭐ | No | Rendimiento nativo sorprendente |
| **Atari 2600** | **StellaDS** | — | ⭐⭐⭐⭐ | No | FluBBaOfWard |
| **ColecoVision** | **ColecoDS** | — | ⭐⭐⭐⭐ | No | FluBBaOfWard |
| **Master System** | **S8DS** | — | ⭐⭐⭐⭐ | No | FluBBaOfWard |
| **Point&Click** | **ScummVM** | — | ⭐⭐⭐⭐ | No | Monkey Island, DOTT, etc. |

### GBARunner2 vs GBARunner3 — Decisión

| Aspecto | GBARunner2 | GBARunner3 |
|---------|:----------:|:----------:|
| Estado | Estable/Legacy | En desarrollo activo |
| Rendimiento | Bueno, probado | Más rápido/optimizado |
| Compatibilidad | Alta, estándar | Mayor, corre juegos que v2 no puede |
| Estabilidad | Muy estable | Variable, puede tener regresiones |
| Setup | Plug & play | Necesita config + `_gba/bios.bin` |

**Recomendación:** Tener **ambos**. GBARunner2 como primario estable, GBARunner3 para títulos problemáticos.

```
/homebrew/gbarunner/
├── GBARunner2.nds        ← Primario
├── GBARunner3.nds        ← Para juegos difíciles
└── bios.bin              ← BIOS GBA (MD5: a860e8c0b6d573d191e4e4444048b000)
```

### Repos de emuladores

| Emulador | GitHub |
|----------|--------|
| GBARunner2 | [github.com/Gericom/GBARunner2](https://github.com/Gericom/GBARunner2) |
| GBARunner3 | [github.com/Gericom/GBARunner3](https://github.com/Gericom/GBARunner3) |
| GameYob | [github.com/Drenn1/GameYob](https://github.com/Drenn1/GameYob) |
| nesDS | [github.com/FluBBaOfWard/nesDS](https://github.com/FluBBaOfWard/nesDS) |
| NitroGrafx | [github.com/FluBBaOfWard/NitroGrafx](https://github.com/FluBBaOfWard/NitroGrafx) |
| StellaDS | [github.com/FluBBaOfWard/StellaDS](https://github.com/FluBBaOfWard/StellaDS) |
| S8DS | [github.com/FluBBaOfWard/S8DS](https://github.com/FluBBaOfWard/S8DS) |
| ScummVM | [github.com/scummvm/scummvm](https://github.com/scummvm/scummvm) |
| SNEmulDS | [gamebrew.org/wiki/SNEmulDS](https://www.gamebrew.org/wiki/SNEmulDS) |
| jEnesisDS | [gamebrew.org/wiki/JEnesisDS](https://www.gamebrew.org/wiki/JEnesisDS) |

---

## 6. 🛠️ Utilidades Esenciales

| App | Función | Tier | Repo |
|-----|---------|:----:|------|
| **GodMode9i** | File browser, dump carts, gestión saves | 🥇 | [GitHub](https://github.com/DS-Homebrew/GodMode9i) |
| **Universal-Updater** | App Store, actualizar homebrew vía WiFi | 🥇 | [GitHub](https://github.com/Universal-Team/Universal-Updater) |
| **DiagnoSe** | Test hardware (pantallas, botones, mic) | 🥈 | [GameBrew](https://www.gamebrew.org/) |
| **DSload** | Transferir archivos PC→DS vía WiFi | 🥉 | [GitHub](https://github.com/Lameguy64/dsload) |

---

## 7. 🎨 Extras y QoL

### Boxart / Carátulas
- Usar **TWiLight Menu++ Offline Updater**
- Resolución ideal: **128×115 px** (NO imágenes grandes, ralentizan el menú)

### Themes
- Usar themes DSi o dark minimal
- Evitar skins pesadas o themes antiguos

### Widescreen (Solo 3DS)
1. Instalar **TWPatch** (vía Universal-Updater)
2. Generar `TwlBg.cxi` → copiar a `/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`
3. En Luma3DS config: activar "Enable external FIRMs and modules"
4. Per-game: Y en juego → Screen Aspect Ratio → 16:10

### Per-Game Settings en TWiLight
- Sobre un juego: **Y** → configuración individual
- Permite ajustar loader, velocidad CPU, aspect ratio por juego

---

## 8. 🎵 Multimedia (Opcional)

| App | Función | Repo |
|-----|---------|------|
| **MoonShell 2.10** | MP3, OGG, videos DPG, imágenes, texto | [DS-Homebrew/moonshell](https://github.com/DS-Homebrew/moonshell) |
| **Colors!** | Dibujo/pintura con touchscreen | [GameBrew](https://www.gamebrew.org/) |
| **NitrousTracker** | Music tracker, fork mejorado de NitroTracker | [GitHub](https://github.com/asiekierka/nitrotracker/) |

> Multimedia es **completamente opcional** en un setup moderno.

---

## 9. 📂 Estructura de Directorios

```
Raíz MicroSD/
│
├── _nds/                         # ← Sistema TWiLight Menu++ (NO tocar)
│   └── TWiLightMenu/
│
├── BOOT.NDS                      # ← TWiLight Menu++ (autoboot via flashcard-bootstrap)
│
├── roms/
│   ├── nds/                      # Juegos DS (.nds) + saves (.sav) MISMA CARPETA
│   ├── gba/                      # ROMs GBA
│   │   └── bios.bin              # BIOS GBA para GBARunner
│   ├── gb/                       # Game Boy
│   ├── gbc/                      # Game Boy Color
│   ├── nes/                      # NES
│   ├── snes/                     # SNES (solo juegos livianos)
│   ├── genesis/                  # Sega Genesis/Mega Drive
│   └── pce/                      # PC Engine / TurboGrafx
│
├── apps/                         # Homebrew y utilidades
│   ├── GodMode9i.nds
│   ├── Universal-Updater.nds
│   ├── DiagnoSe.nds
│   └── emulators/
│       ├── GBARunner2.nds
│       ├── GBARunner3.nds
│       ├── GameYob.nds
│       ├── nesDS.nds
│       ├── SNEmulDS.nds
│       ├── jEnesisDS.nds
│       ├── NitroGrafx.nds
│       └── ScummVM.nds
│
├── media/                        # MoonShell media (opcional)
│
├── backup/                       # Respaldos críticos
│   ├── saves/                    # Copia periódica de saves
│   ├── configs/                  # .ini, configs TWiLight
│   └── kernel/                   # Kernel original de respaldo
│
└── [archivos kernel R4]          # flashcard-bootstrap o YSMenu
    └── (varían según modelo)
```

### Reglas de la estructura:
1. **Saves (.sav) en MISMA carpeta que .nds** — Configurar TWiLight para esto → evita duplicados con YSMenu
2. **BIOS GBA** en `/roms/gba/` Y en `/_nds/` para máxima compatibilidad
3. **10% espacio libre** siempre — previene corrupción al guardar
4. **NO** carpetas con nombres con espacios o caracteres especiales

---

## 10. 📥 Guía de Instalación

### Paso 1: Preparar MicroSD
1. Formatear con GUIFormat → FAT32, 32KB clusters, MBR
2. Verificar con H2testw (escribir + leer completo)

### Paso 2: Instalar kernel R4
1. Identificar modelo exacto de R4
2. Descargar flashcard-bootstrap release → [GitHub Releases](https://github.com/lifehackerhansol/flashcard-bootstrap/releases)
3. Copiar archivos correspondientes a tu modelo a la raíz

### Paso 3: Instalar TWiLight Menu++
1. Descargar `TWiLightMenu-Flashcard.7z` → [GitHub Releases](https://github.com/DS-Homebrew/TWiLightMenu/releases)
2. Extraer `_nds/`, `BOOT.NDS` a la raíz
3. Si hay carpeta `Autoboot/` dentro, buscar tu modelo y copiar contenido
4. nds-bootstrap viene incluido dentro del paquete TWiLight

### Paso 4: Agregar utilidades
1. Descargar GodMode9i.nds → [Releases](https://github.com/DS-Homebrew/GodMode9i/releases) → a `/apps/`
2. Descargar Universal-Updater → [Releases](https://github.com/Universal-Team/Universal-Updater/releases) → a `/apps/`

### Paso 5: Agregar emuladores
1. Descargar cada .nds de los repos listados en sección 5
2. Colocar en `/apps/emulators/`
3. Copiar `bios.bin` GBA a `/roms/gba/` y `/_nds/`

### Paso 6: Agregar
- **Soft Reset:** `L+R+Down+B` (Regresa al menú de TWiLight desde un juego)
- **Carga Rápida:** Los ROMs se parchean al vuelo, sin esperas.

### Paso 7: Organizar ROMs
1. Crear estructura de carpetas como sección 9
2. Colocar ROMs No-Intro limpias en cada carpeta
3. Verificar primer boot

### Paso 8: Backup inicial
1. Copiar TODO el contenido de la SD a PC como "backup day-0"

---

## 11. ⚙️ Configuración Avanzada TWiLight

### Settings globales importantes
- **Loader:** nds-bootstrap (primario) / kernel de flashcard (fallback)
- **Saves location:** "Same folder as ROM" ← **CRÍTICO** para evitar duplicados
- **AP Fix:** Auto (dejar que nds-bootstrap lo maneje)
- **Theme:** DSi o Saturn (rápidos, limpios)
- **Boxart:** Activar si ya están procesadas a 128×115

### Per-game (botón Y sobre un juego)
- Cambiar loader si un juego falla con nds-bootstrap → usar kernel flashcard
- Ajustar ARM9 CPU Speed para juegos que lo necesiten
- Activar VRAM Boost si hay problemas gráficos

### Cheats (botón X sobre un juego)
- Requiere `usrcheat.dat` instalado
- Toggle cheats con A, guardar con X

---

## 12. 💾 Mantenimiento y Backups

### Prioridad de backup

| Prioridad | Qué | Frecuencia |
|:---------:|-----|-----------|
| 🔴 Crítico | `/roms/nds/*.sav` (saves de juegos) | Semanal o antes de cambios |
| 🟡 Alto | `/_nds/` (config TWiLight) | Mensual |
| 🟢 Normal | Todo lo demás | Trimestral |

### Regla de actualización

```
Si funciona bien → NO actualices.
Actualizar solo si:
  - Bug que te afecta
  - Incompatibilidad nueva
  - Mejora relevante (ej: juego que no corría)
```

### Revisar releases de:
- [nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap/releases)
- [TWiLight Menu++](https://github.com/DS-Homebrew/TWiLightMenu/releases)
- [GBARunner2](https://github.com/Gericom/GBARunner2/releases) / [GBARunner3](https://github.com/Gericom/GBARunner3)

---

## 13. 📊 Matriz por Consola

| Consola destino | Boot | GBA nativo | Slot-2 | Widescreen | Mejor para |
|:---:|:---:|:---:|:---:|:---:|---|
| **DS Fat** | R4 + TWiLight | Via GBARunner2 | ✅ (3-in-1 pak) | ❌ | Compatibilidad Slot-2 |
| **DS Lite** | R4 + TWiLight | Via GBARunner2 + Slot-2 nativo | ✅ | ❌ | Mejor experiencia GBA (Slot-2 nativo) |
| **DSi** | R4 + TWiLight | Via GBARunner2/3 | ❌ | ❌ | Mejor rendimiento general, WiFi WPA |
| **3DS / 2DS** | R4 + TWiLight | Via GBARunner2/3 | ❌ | ✅ (TWPatch) | Mejor experiencia total, widescreen |

### Nota sobre Slot-2 (Solo DS/DS Lite)
Si tienes DS Lite, el combo **R4 (Slot-1) + EZ-Flash 3-in-1 (Slot-2)** es el gold standard:
- Slot-1: NDS, homebrew, emuladores
- Slot-2: GBA nativo real, RAM expansion, Rumble

---

## 14. 🚫 Qué NO Incluir

- ❌ Kernels oficiales viejos como sistema principal
- ❌ Wood R4 como launcher principal (legacy)
- ❌ Homebrew abandonado que no uses
- ❌ Emuladores duplicados (ej: Lameboy SI ya tienes GameYob)
- ❌ Packs gigantes desordenados de internet
- ❌ Themes pesados con animaciones
- ❌ ROMs trimmeadas o pre-parcheadas
- ❌ Llenar la SD al 100%
- ❌ Apps redundantes "por si acaso"

---

## 15. 🏆 Resumen Ejecutivo

### Stack definitivo

```
┌─────────────────────────────────────────┐
│          CAPA 3: CONTENIDO              │
│  ROMs · Saves · Cheats · Boxart         │
├─────────────────────────────────────────┤
│          CAPA 2: SISTEMA                │
│  TWiLight Menu++ · nds-bootstrap        │
│  GodMode9i · Universal-Updater          │
├─────────────────────────────────────────┤
│          CAPA 1: EMULACIÓN              │
│  GBARunner2/3 · GameYob · nesDS         │
│  SNEmulDS · jEnesisDS · NitroGrafx      │
├─────────────────────────────────────────┤
│          CAPA 0: BOOT                   │
│  flashcard-bootstrap → BOOT.NDS         │
│  (YSMenu como fallback)                 │
├─────────────────────────────────────────┤
│          HARDWARE                       │
│  R4 Flashcart · MicroSD FAT32 32KB      │
│  NDS/DS Lite/DSi/3DS                    │
└─────────────────────────────────────────┘
```

### Este setup permite:

| Capacidad | Detalle |
|-----------|---------|
| 🎮 Juegos NDS | Catálogo completo desde SD con AP patch automático |
| 🕹️ Retro 8-bit | NES, GB, GBC, Master System, Atari 2600, ColecoVision |
| 🕹️ Retro 16-bit | SNES (parcial), Genesis, PC Engine |
| 🎮 GBA | Compatibilidad alta vía GBARunner2/3 |
| 🔧 Mantenimiento | GodMode9i para archivos, Universal-Updater para updates |
| 🎨 Personalización | Themes, boxart, cheats, per-game config |
| 📺 Widescreen | En 3DS con TWPatch |
| 💾 Saves seguros | Estructura unificada, backup fácil |
| 🔄 Actualizaciones | Via WiFi con Universal-Updater o manual |

### Requiere:

| Item | Detalle |
|------|---------|
| **Hardware** | NDS/Lite/DSi/3DS + Flashcart R4 compatible |
| **MicroSD** | 32GB SDHC Class 10, FAT32, MBR |
| **PC** | Para formateo inicial, transferencia de archivos, backups |
| **BIOS GBA** | Dump de `bios.bin` para GBARunner (opcional pero recomendado) |
| **WiFi** | WEP/Open para Universal-Updater (opcional) |

---

## 📚 Referencias y Links Maestros

| Recurso | Link |
|---------|------|
| DS-Homebrew (org principal) | [github.com/DS-Homebrew](https://github.com/DS-Homebrew) |
| TWiLight Menu++ | [github.com/DS-Homebrew/TWiLightMenu](https://github.com/DS-Homebrew/TWiLightMenu) |
| nds-bootstrap | [github.com/DS-Homebrew/nds-bootstrap](https://github.com/DS-Homebrew/nds-bootstrap) |
| flashcard-bootstrap | [github.com/lifehackerhansol/flashcard-bootstrap](https://github.com/lifehackerhansol/flashcard-bootstrap) |
| Flashcard Archive (kernels) | [github.com/flashcarts/flashcard-archive](https://github.com/flashcarts/flashcard-archive) |
| Universal-Updater | [github.com/Universal-Team/Universal-Updater](https://github.com/Universal-Team/Universal-Updater) |
| DS-Homebrew Wiki | [ds-homebrew.com](https://ds-homebrew.com/) |
| GameBrew (todo homebrew) | [gamebrew.org](https://www.gamebrew.org/) |
| GBAtemp (foro comunidad) | [gbatemp.net](https://gbatemp.net/) |
| awesome-dsdev | [github.com/asiekierka/awesome-dsdev](https://github.com/asiekierka/awesome-dsdev) |
| Guía CFW DSi | [dsi.cfw.guide](https://dsi.cfw.guide/) |
| TWiLight Flashcard Install Guide | [wiki.ds-homebrew.com](https://wiki.ds-homebrew.com/twilightmenu/installing-flashcard) |

---

> **Este es el setup definitivo.** Cualquier adición futura debería pasar el test:
> *"¿Realmente lo voy a usar, o es bloat?"*
