import os
import shutil
import subprocess
import time

def clear_and_create(path):
    for i in range(5):
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
            os.makedirs(path)
            return
        except PermissionError:
            time.sleep(0.5)
    os.makedirs(path, exist_ok=True)

def extract_file(filepath, extract_to):
    print(f"Descomprimiendo {os.path.basename(filepath)}...")
    os.makedirs(extract_to, exist_ok=True)
    result = subprocess.run(['tar', '-xf', filepath, '-C', extract_to], capture_output=True)
    return result.returncode == 0

def clean_bloat(base_path):
    print("Iniciando limpieza selectiva (No-Cheats)...")
    # Solo borramos lo que REALMENTE es basura o no queremos (Cheats)
    folders_to_remove = [
        "_nds/TWiLightMenu/extras",
        "_nds/TWiLightMenu/cheats"
    ]
    files_to_remove = [
        "BOOT_ALT.NDS",
        "nds-bootstrap-hb-release.nds"
    ]

    for folder in folders_to_remove:
        path = os.path.join(base_path, folder)
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"  - Eliminado: {folder}")

    for file in files_to_remove:
        path = os.path.join(base_path, file)
        if os.path.exists(path):
            os.remove(path)
            print(f"  - Eliminado: {file}")

def main():
    root_path = os.getcwd()
    build_path = os.path.join(root_path, "build/SD_Final")
    download_dir = os.path.join(root_path, "build/downloads")
    temp_extract = os.path.join(root_path, "build/temp_extract")
    
    clear_and_create(build_path)

    # 1. Estructura Base
    print("Cargando estructura base...")
    shutil.copytree("templates/sd_structure", build_path, dirs_exist_ok=True)

    # 2. Configs Personales
    print("Inyectando bootloaders y configuraciones...")
    for file in os.listdir("templates/bootloaders"):
        shutil.copy(os.path.join("templates/bootloaders", file), build_path)
    
    for file in os.listdir("templates/configs"):
        if "snemul" in file:
            shutil.copy(os.path.join("templates/configs", file), build_path)
        else:
            dest_dir = os.path.join(build_path, "_nds")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy(os.path.join("templates/configs", file), os.path.join(dest_dir, file))

    # 3. Descargas
    if os.path.exists(download_dir):
        for file in os.listdir(download_dir):
            filepath = os.path.join(download_dir, file)
            if file.endswith(".nds"):
                shutil.copy(filepath, os.path.join(build_path, "apps", file))
            elif file.endswith(".7z") or file.endswith(".zip"):
                clear_and_create(temp_extract)
                if extract_file(filepath, temp_extract):
                    shutil.copytree(temp_extract, build_path, dirs_exist_ok=True)
    
    # 4. Limpieza (Mantenemos Autoboot y Flashcart Loader para compatibilidad)
    clean_bloat(build_path)

    # Limpieza final de temp
    if os.path.exists(temp_extract):
        try:
            shutil.rmtree(temp_extract)
        except:
            pass

    print(f"\n[OK] Build terminado (Compatible y sin Cheats) en: {build_path}")

if __name__ == "__main__":
    main()
