import requests
import os
import json

def get_latest_release_asset(repo, pattern):
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        response = requests.get(api_url)
        if response.status_code != 200:
            print(f"DEBUG: {repo} no tiene releases oficiales o es privado.")
            return None, None
        
        data = response.json()
        assets = data.get('assets', [])
        
        # DEBUG: Imprimir qué archivos hay si no encontramos el patrón
        found_names = [a['name'] for a in assets]
        
        for asset in assets:
            if pattern.lower() in asset['name'].lower():
                return asset['browser_download_url'], asset['name']
        
        if assets:
            print(f"DEBUG: En {repo} se encontraron: {', '.join(found_names)} pero ninguno coincide con '{pattern}'")
            
    except Exception as e:
        print(f"Error en {repo}: {e}")
    return None, None

def download_file(url, dest):
    print(f"Descargando: {url}...")
    response = requests.get(url, stream=True)
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def main():
    with open("manifest.json", 'r') as f:
        manifest = json.load(f)

    os.makedirs("build/downloads", exist_ok=True)

    for tool in manifest['tools']:
        url, filename = get_latest_release_asset(tool['repo'], tool['asset_pattern'])
        if url:
            dest = os.path.join("build/downloads", filename)
            if not os.path.exists(dest):
                download_file(url, dest)
            else:
                print(f"Ya existe: {filename}")
        else:
            # Si falla, no hacemos nada extra, el DEBUG de arriba ya nos dirá qué pasó
            pass

if __name__ == "__main__":
    main()
