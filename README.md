# R4-ABS (Auto-Build System)

Sistema automatizado para la creación y mantenimiento del setup definitivo de MicroSD para flashcarts R4 (NDS).

## 🎯 Objetivo
Eliminar la gestión manual de archivos. Este repositorio utiliza **GitHub Actions** para descargar, configurar y empaquetar automáticamente las últimas versiones de:
- **TWiLight Menu++** (Launcher)
- **nds-bootstrap** (Kernel/Loader)
- **Emuladores** (NES, GB, GBC, SNES, GBA, etc.)
- **Herramientas de sistema** (GodMode9i)

## ⚠️ Requisito Crítico
Para que la R4 reconozca la MicroSD, esta **DEBE** estar formateada con:
- **Sistema de archivos:** FAT32
- **Tabla de particiones:** MBR
- **Cluster size:** 32KB (recomendado)

## 🚀 Cómo obtener el setup
No es necesario ejecutar nada localmente. Ve a la sección de **Releases** de este repositorio y descarga el archivo `.zip` más reciente.
1. Extrae el contenido en la raíz de tu MicroSD.
2. Añade tus juegos en la carpeta `/roms/`.
3. ¡Listo para jugar!

---
*Automatizado mensualmente con GitHub Actions.*
