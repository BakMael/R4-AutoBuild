# 🚀 Propuesta: NDS R4 Auto-Build System (R4-ABS)

Este documento detalla el planteamiento para la creación de un repositorio automatizado capaz de generar, mantener y actualizar el "Setup Definitivo" de una MicroSD para R4 de forma autónoma.

---

## 1. 💡 La Idea
Transformar el proceso de configuración de una R4 de una tarea manual y propensa a errores (descargar 10+ archivos de sitios distintos) a un **proceso de integración continua (CI)**. 

En lugar de tener una carpeta con archivos viejos en el PC, tendremos un repositorio en GitHub que "sabe" dónde están las últimas versiones de cada herramienta y las ensambla por nosotros en un paquete listo para usar.

---

## 2. ⚙️ Funcionalidad

El sistema operaría bajo un flujo de **"Fetch & Overlay"**:

1.  **Tracking Upstream:** El sistema monitorea los repositorios oficiales de la comunidad (DS-Homebrew, Universal-Team, Gericom, etc.).
2.  **Automated Assembly:** 
    - Un script descarga los últimos binarios (`.nds`) y archivos de sistema.
    - Descomprime paquetes complejos (como TWiLight Menu++).
    - Organiza los archivos en la estructura de carpetas optimizada que definimos (`/apps/`, `/_nds/`, `/roms/`, etc.).
3.  **Config Injection:** Aplica tus configuraciones personales (idioma, temas, `snemul.cfg`) sobre los archivos nuevos.
4.  **Artifact Generation:** Genera un archivo `.zip` único (ej: `R4-Setup-v2026.05.09.zip`) como un "Release" de GitHub.

---

## 3. 🎯 Meta
- **Mantenimiento Cero:** No volver a buscar "¿cuál es la última versión de nds-bootstrap?" manualmente.
- **Reproducibilidad:** Garantizar que cada vez que configures una SD nueva, obtengas exactamente el mismo resultado optimizado.
- **Limpieza (Zero-Bloat):** El script solo incluye lo esencial, eliminando archivos innecesarios que suelen venir en los packs genéricos de internet.
- **Versionado:** Poder "volver atrás" a una versión anterior si una actualización rompe compatibilidad con un juego específico.

---

## 4. ⚠️ Limitaciones y Desafíos

### A. Legalidad y ROMs
- **Limitación:** No se pueden incluir ROMs de juegos comercializados ni archivos de BIOS (como `bios.bin` de GBA) directamente en el repositorio público de GitHub por riesgos de copyright (DMCA).
- **Solución:** El repositorio genera la "estructura" y las herramientas. El usuario final debe añadir su carpeta `/roms/` y su `bios.bin` manualmente (o mediante un script privado).

### B. Fuentes No-GitHub
- **Limitación:** Algunos emuladores clásicos o kernels específicos (como YSMenu) solo están en GameBrew o hilos de GBAtemp, que no tienen una API fácil para descargas automatizadas.
- **Solución:** Estos archivos se manejarían como "Componentes Estáticos" dentro del repo o se usarían técnicas de web scraping básico si es estrictamente necesario.

### C. Especificidad del Hardware
- **Limitación:** Existen cientos de modelos de R4. Un solo "Auto-Build" podría no servir para todos si el kernel primario es distinto.
- **Solución:** El build generará una carpeta `/kernels/` con las opciones más comunes (flashcard-bootstrap, BL2CK, YSMenu) para que el usuario elija la que corresponde a su tarjeta.

---

## 5. 🛠️ Próximos Pasos (Hoja de Ruta)

1.  **Definir el "Manifiesto":** Un archivo JSON/YAML que liste todos los repositorios a seguir.
2.  **Preparar los "Static Assets":** Subir las carpetas de estructura y archivos de configuración que no cambian.
3.  **Desarrollar el Script de Ensamblaje:** Script en Python para la lógica de descarga y organización.
4.  **Configurar GitHub Actions:** Automatizar la ejecución para que se dispare con un botón o de forma programada.

---
> *Documento generado para el proyecto de automatización NDS R4.*
