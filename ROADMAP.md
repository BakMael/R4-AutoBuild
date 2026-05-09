# 🗺️ Hoja de Ruta: NDS R4 Ultimate Repo

Este archivo registra el progreso del proyecto. Una vez que el repositorio esté configurado y subido a Git, este archivo puede ser eliminado.

## 🟢 Fase 1: Preparación Local y Plantillas
- [x] **Rescatar archivos "Llave"**: Copiar `R4.dat` y `TTMenu.dat` desde la SD `I:\` a `templates/bootloaders/`.
- [x] **Extraer Configuraciones**: Guardar `snemul.cfg` y archivos `.ini` personalizados en `templates/configs/`.
- [x] **Crear Manifiesto de Herramientas**: Definir `manifest.json` con los repos de GitHub a monitorear.
- [x] **Estructura Base de SD**: Crear un esqueleto de carpetas en `templates/sd_structure/`.

## 🟡 Fase 2: Automatización (Scripts)
- [x] **Script de Consulta (GitHub API)**: Python script para obtener las URLs de los últimos releases.
- [x] **Lógica de Descarga y Extracción**: Soporte para archivos `.zip` y `.7z`.
- [x] **Script de Ensamblaje (Build)**: Unificar descargas + plantillas en una carpeta final lista para usar.

## 🔍 Fase de Validación y Pruebas (LOCAL)
- [ ] **Transferencia a SD**: Copiar `build/SD_Final` a la MicroSD física.
- [ ] **Prueba de Arranque**: Confirmar que la R4 inicia directamente en TWiLight Menu++.
- [ ] **Verificación de Emuladores**: Probar que los emuladores estáticos abren correctamente.
- [ ] **Verificación de Herramientas**: Abrir GodMode9i desde la carpeta `apps`.
- [ ] **Ajuste de Configs**: Validar que el idioma y temas se aplicaron bien.

## 🔵 Fase 3: Configuración de Git y Publicación
- [x] **Inicializar Git**: `git init` en la raíz.
- [x] **Verificar .gitignore**: Confirmar que no se suban ROMs, Saves o BIOS.
- [x] **Primer Commit**: Guardar la estructura base limpia.
- [ ] **Segundo Commit**: Guardar scripts funcionales y limpieza Zero-Bloat.
- [ ] **Conexión Remota**: Vincular con un repositorio en GitHub.

## ⚪ Fase 4: Pulido y Extras
- [ ] **GitHub Actions**: Configurar workflow para builds automáticos en la nube.
- [ ] **Wiki/Documentación**: Expandir `RECURSOS.md` con guías de uso de emuladores.

---
> *Última actualización: 2026-05-09*
