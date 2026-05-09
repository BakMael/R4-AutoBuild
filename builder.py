import os
import shutil
import json
import requests
import subprocess
import time
import logging

# Configuración de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger("R4Builder")

class R4Builder:
    def __init__(self, manifest_path="manifest.json", build_dir="build"):
        self.root_path = os.getcwd()
        self.manifest_path = os.path.join(self.root_path, manifest_path)
        self.build_dir = os.path.join(self.root_path, build_dir)
        self.download_dir = os.path.join(self.build_dir, "downloads")
        self.sd_final_dir = os.path.join(self.build_dir, "SD_Final")
        self.temp_extract = os.path.join(self.build_dir, "temp_extract")
        self.manifest = self._load_manifest()

    def _load_manifest(self):
        if not os.path.exists(self.manifest_path):
            logger.error(f"No se encontró {self.manifest_path}")
            return None
        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def _clear_and_create(self, path):
        for i in range(5):
            try:
                if os.path.exists(path):
                    shutil.rmtree(path)
                os.makedirs(path)
                return
            except PermissionError:
                time.sleep(0.5)
        os.makedirs(path, exist_ok=True)

    def fetch_tools(self):
        logger.info("--- Iniciando descarga de herramientas dinámicas ---")
        os.makedirs(self.download_dir, exist_ok=True)
        
        for tool in self.manifest['tools']:
            url, filename = self._get_latest_release(tool['repo'], tool['asset_pattern'])
            if url:
                dest = os.path.join(self.download_dir, filename)
                if not os.path.exists(dest):
                    self._download_file(url, dest)
                else:
                    logger.info(f"  - {tool['name']} ya está actualizado.")
            else:
                logger.warning(f"  - No se pudo encontrar release para {tool['name']}")

    def _get_latest_release(self, repo, pattern):
        api_url = f"https://api.github.com/repos/{repo}/releases/latest"
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            for asset in data.get('assets', []):
                if pattern.lower() in asset['name'].lower():
                    return asset['browser_download_url'], asset['name']
        except Exception as e:
            logger.debug(f"Error consultando {repo}: {e}")
        return None, None

    def _download_file(self, url, dest):
        logger.info(f"  - Descargando {os.path.basename(dest)}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dest, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    def assemble(self):
        logger.info("--- Iniciando ensamblaje de la SD ---")
        self._clear_and_create(self.sd_final_dir)

        # 1. Base Structure
        logger.info("  - Aplicando estructura base...")
        shutil.copytree("templates/sd_structure", self.sd_final_dir, dirs_exist_ok=True)

        # 2. Bootloaders and Configs
        logger.info("  - Inyectando archivos del sistema y configuraciones...")
        for file in os.listdir("templates/bootloaders"):
            shutil.copy(os.path.join("templates/bootloaders", file), self.sd_final_dir)
        
        for file in os.listdir("templates/configs"):
            if "snemul" in file:
                shutil.copy(os.path.join("templates/configs", file), self.sd_final_dir)
            else:
                dest_config = os.path.join(self.sd_final_dir, "_nds", file)
                shutil.copy(os.path.join("templates/configs", file), dest_config)

        # 3. Dynamic Tools
        for tool in self.manifest['tools']:
            # Lógica de búsqueda de archivo descargado
            for file in os.listdir(self.download_dir):
                if tool['asset_pattern'].lower() in file.lower():
                    filepath = os.path.join(self.download_dir, file)
                    if file.endswith(".nds"):
                        shutil.copy(filepath, os.path.join(self.sd_final_dir, tool['target_dir'].strip('/'), file))
                    elif file.endswith(".7z") or file.endswith(".zip"):
                        self._extract_and_merge(filepath, self.sd_final_dir)

        self.clean_bloat()
        logger.info(f"[SUCCESS] Build completado en {self.sd_final_dir}")

    def _extract_and_merge(self, filepath, dest):
        self._clear_and_create(self.temp_extract)
        subprocess.run(['tar', '-xf', filepath, '-C', self.temp_extract], capture_output=True)
        shutil.copytree(self.temp_extract, dest, dirs_exist_ok=True)
        try:
            shutil.rmtree(self.temp_extract)
        except:
            pass

    def clean_bloat(self):
        logger.info("  - Ejecutando limpieza Zero-Bloat...")
        to_remove = [
            "_nds/TWiLightMenu/extras",
            "_nds/TWiLightMenu/cheats",
            "BOOT_ALT.NDS",
            "nds-bootstrap-hb-release.nds"
        ]
        for item in to_remove:
            path = os.path.join(self.sd_final_dir, item)
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

if __name__ == "__main__":
    builder = R4Builder()
    if builder.manifest:
        builder.fetch_tools()
        builder.assemble()
