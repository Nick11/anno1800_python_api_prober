# Anno 1800 Python API Prober
A simple python script to reverse-engineer the Anno 1800 python API.

It allows you to change the `debugger.py`file while the game is running and write debugging info to the `debug.log` file.

## Install
- Install the **Anno 1800 Mod Loader** https://github.com/xforce/anno1800-mod-loader
- Also checkout the **Spice it up** Mod collection to get some working samples of mods. https://www.nexusmods.com/anno1800/mods/5?tab=description
- Copy the *[DEBUG] API PROBER* directory from the *src* to your Anno 1800 mod directory (See **Anno 1800 Mod Loader** for instructions. Usually you create a *mod* directory at *C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\games\Anno 1800*
- Then edit *[DEBUG] API PROBER/Prober/start_script.py"* line 5 `self.src_path = "C:/code/anno1800_modding/src"`, set the `src_path` to the directory, where the `debugger.py` file is.

## How to use
The mod binds the Num Pad keys 7 to 9 to send python objects from the Anno API to the `debugger.py` script (`start_script.py` does that).
You can freely edit the `debugger.py` script while the game is running, the `start_script.py` is loaded during the game startup though.

## ANNO 1800 Python API
It seems Anno 1800 is using a Python API internally. The resourceful brains behind  **Anno 1800 Mod Loader** found a way to tap onto this API.

PYTHON_API.md contains some of my limited insights.