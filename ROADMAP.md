# 🗺️ Hoja de Ruta: NDS R4 Ultimate Repo

Este archivo registra el progreso del proyecto. Una vez que el repositorio esté configurado y subido a Git, este archivo puede ser eliminado.

## 🟢 Fase 1: Preparación Local y Plantillas
- [x] **Rescatar archivos "Llave"**: Copiar `R4.dat` y `TTMenu.dat` desde la SD `I:\` a `templates/bootloaders/`.
- [x] **Extraer Configuraciones**: Guardar `snemul.cfg` y archivos `.ini` personalizados en `templates/configs/`.
- [x] **Crear Manifiesto de Herramientas**: Definir `manifest.json` con los repos de GitHub a monitorear.
- [x] **Estructura Base de SD**: Crear un esqueleto de carpetas en `templates/sd_structure/`.

## 🟡 Fase 2: Automatización (Scripts)
- [ ] **Script de Consulta (GitHub API)**: Python script para obtener las URLs de los últimos releases.
- [ ] **Lógica de Descarga y Extracción**: Soporte para archivos `.zip` y `.7z`.
- [ ] **Script de Ensamblaje (Build)**: Unificar descargas + plantillas en una carpeta final lista para usar.

## 🔵 Fase 3: Configuración de Git
- [ ] **Inicializar Git**: `git init` en la raíz.
- [ ] **Verificar .gitignore**: Confirmar que no se suban ROMs, Saves o BIOS.
- [ ] **Primer Commit**: Guardar la estructura base limpia.
- [ ] **Conexión Remota**: Vincular con un repositorio en GitHub.

## ⚪ Fase 4: Pulido y Extras
- [ ] **GitHub Actions**: Configurar workflow para builds automáticos en la nube.
- [ ] **Wiki/Documentación**: Expandir `RECURSOS.md` con guías de uso de emuladores.

---
> *Última actualización: 2026-05-09*
