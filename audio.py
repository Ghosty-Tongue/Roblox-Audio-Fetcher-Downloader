import requests
import time
import re
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

def fetch_audio_location(asset_id, place_id, roblox_cookie):
    while True:
        body_array = [{
            "assetId": asset_id,
            "assetType": "Audio",
            "requestId": "0"
        }]

        headers = {
            "User-Agent": "Roblox/WinInet",
            "Content-Type": "application/json",
            "Cookie": f".ROBLOSECURITY={roblox_cookie}",
            "Roblox-Place-Id": place_id,
            "Accept": "*/*",
            "Roblox-Browser-Asset-Request": "false"
        }

        response = requests.post('https://assetdelivery.roblox.com/v2/assets/batch', headers=headers, json=body_array)

        if response.status_code == 200:
            locations = response.json()
            if locations and len(locations) > 0:
                obj = locations[0]
                if obj.get("locations") and obj["locations"][0].get("location"):
                    return obj["locations"][0]["location"]

        # Wait before retrying
        time.sleep(0.5)

def sanitize_filename(name):
    sanitized_name = re.sub(r'[\\/*?"<>|]', '', name)
    sanitized_name = sanitized_name.replace(" ", "_")  # Replace spaces with underscores
    return sanitized_name

def fetch_asset_name(asset_id):
    while True:
        response = requests.get(f"https://economy.roproxy.com/v2/assets/{asset_id}/details")
        if response.status_code == 200:
            asset_info = response.json()
            asset_name = asset_info.get("Name")
            if asset_name:
                return asset_name
        # Wait before retrying
        time.sleep(0.5)

def download_audio_files(roblox_cookie, place_id, asset_ids):
    for asset_id in asset_ids:
        try:
            asset_name = fetch_asset_name(asset_id)
            sanitized_asset_name = sanitize_filename(asset_name)
            audio_url = fetch_audio_location(asset_id, place_id, roblox_cookie)

            if audio_url:
                response = requests.get(audio_url)
                if response.status_code == 200:
                    # Create a folder for downloaded audio files
                    os.makedirs("audio_files", exist_ok=True)

                    file_path = os.path.join("audio_files", sanitized_asset_name + ".ogg")

                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(Fore.GREEN + f"Downloaded: {sanitized_asset_name}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Failed to download: {sanitized_asset_name}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"Audio URL not found for: {sanitized_asset_name}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error downloading {asset_id}: {e}" + Style.RESET_ALL)

def main():
    roblox_cookie = input(Fore.CYAN + "Enter Roblox Cookie (.ROBLOSECURITY): " + Style.RESET_ALL)
    place_id = input(Fore.CYAN + "Enter Place ID: " + Style.RESET_ALL)
    
    while True:
        asset_ids_input = input(Fore.CYAN + "Enter asset IDs (comma-separated, e.g., 123,456,789) or type 'exit' to quit: " + Style.RESET_ALL)
        
        if asset_ids_input.lower() == 'exit':
            print(Fore.CYAN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break
        
        asset_ids = asset_ids_input.split(',')
        download_audio_files(roblox_cookie, place_id, asset_ids)
        
        print(Fore.CYAN + "All specified audio assets have been downloaded." + Style.RESET_ALL)

if __name__ == "__main__":
    main()