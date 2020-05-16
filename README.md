# Anno 1800 Python API Prober
A simple python script to reverse-engineer the Anno 1800 python API.

It allows you to change the `debugger.py`file while the game is running and write debugging info to the `debug.log` file.

## Install
- Install the **Anno 1800 Mod Loader** https://github.com/xforce/anno1800-mod-loader
- Also checkout the **Spice it up** Mod collection to get some working samples of mods. https://www.nexusmods.com/anno1800/mods/5?tab=description
- Copy the *[DEBUG] API PROBER* directory from the *src* to your Anno 1800 mod directory (See **Anno 1800 Mod Loader** for instructions. Usually you create a *mod* directory at *C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\games\Anno 1800*
- Then edit *[DEBUG] API PROBER/Prober/start_script.py"* line 5 `self.src_path = "C:/code/anno1800_modding/src"`, set the `src_path` to the directory, where the `debugger.py` file is.

## How to use
The mod binds the "I" key to send all loaded python-modules to the `debugger.py` script (`start_script.py` does that).

You can freely edit the `debugger.py` script while the game is running, the `start_script.py` is loaded during the game startup though.

## ANNO 1800 Python API
It seems Anno 1800 is using a Python API internally. The resourceful brains behind  **Anno 1800 Mod Loader** found a way to tap onto this API.

PYTHON_API.md contains some of my limited insights.

## More useful info
### quickbms
quickbms allows you to extract the game data containers (Data0.rda, ..., Patch1.rda) found in *Ubisoft Game Launcher\games\Anno 1800\maindata*.

- Download  quickbms and the Anno5 script from http://aluigi.altervista.org/quickbms.htm

Find an overview of the data-structure here : https://anno1800.fandom.com/wiki/Modding

### assets.xml
Once extracted from Data0.rda, find ths `asset.xml` at `<data extracted from Data0>\config\export\main\asset`

### read_assets.py
`src/read_asset.py` is a simple parser for the assets.xml that generates a list of all products. (`asset_list.py`)

### open Anno 1800 console
Anno 1800 has an in-game console where you can access the Python API.
In the python script execute `dir()['console'].toggleVisibility()` or `console.toggleVisibility()`
