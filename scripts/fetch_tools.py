import requests
import os
import json
import subprocess

def get_latest_release_asset(repo, pattern):
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        for asset in data.get('assets', []):
            if pattern.lower() in asset['name'].lower():
                return asset['browser_download_url'], asset['name']
    except:
        pass
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
            print(f"Error: {tool['name']} no encontrado en GitHub.")

if __name__ == "__main__":
    main()
