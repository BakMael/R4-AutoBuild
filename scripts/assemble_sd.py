import os
import shutil
import json
import subprocess

def clear_and_create(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def main():
    build_path = "build/SD_Final"
    clear_and_create(build_path)

    # 1. Copiar Estructura Base
    print("Aplicando estructura base...")
    shutil.copytree("templates/sd_structure", build_path, dirs_exist_ok=True)

    # 2. Copiar Bootloaders y Configs
    print("Inyectando bootloaders y configuraciones...")
    for file in os.listdir("templates/bootloaders"):
        shutil.copy(os.path.join("templates/bootloaders", file), build_path)
    
    for file in os.listdir("templates/configs"):
        # Determinar destino basado en el nombre del archivo
        if "snemul" in file:
            shutil.copy(os.path.join("templates/configs", file), build_path)
        else:
            dest = os.path.join(build_path, "_nds", file)
            shutil.copy(os.path.join("templates/configs", file), dest)

    # 3. Procesar descargas (Simplificado para este prototipo)
    print("Organizando herramientas descargadas...")
    with open("manifest.json", 'r') as f:
        manifest = json.load(f)

    for tool in manifest['tools']:
        # Aquí iría la lógica de extracción y movimiento según target_dir
        # Para este ejemplo, solo imprimimos el plan
        print(f"Preparado para mover {tool['name']} a {tool['target_dir']}")

    print("\n✅ Proceso de ensamblaje completado (Fase de prototipo).")

if __name__ == "__main__":
    main()
