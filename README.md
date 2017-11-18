[ST3] Launch ConEmu64(CMD) of the CMDER instalation from Sublime Text 3
=================================
Only works for sublime text 3 on windows!

## Features
* Support project, folder, and even files-only instance!
* Support context menu on sidebar's folder or file 
* Reuse ConEmu window and try to open in a new tab
* Open ConEmu tab with a contextual title, like `st:<project name>` and `st:<project name>: <folder relative path to the project>`

## Installation
1º - You should install the CMDER from (http://cmder.net/) first, and add `ConEmu64.exe` to the `%PATH%` environment var.

2º - Copy this project to the Sublime Text 3 Packages directory:

"C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\Packages\"

3º - Make sure the path to the "ConEmuOpen.py" file looks like this:

"C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\Packages\Sublime_ConEmuOpen\ConEmuOpen.py"

## Usage
* Use `ctrl+shift+1` to open current file's folder, `ctrl+1` to open the project or top folder.
* Command palette commands: `ConEmu: Open current file folder` and `ConEmu: Open project or top folder`.

## License :

Licensed under MIT

Copyright (c) 2015 [kiliwalk](https://github.com/kiliwalk)
