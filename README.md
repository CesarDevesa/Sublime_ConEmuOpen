[ST3] Launch ConEmu(CMD or PowerShell) of the CMDER instalation from Sublime Text 3
=================================
Only works for sublime text 3 on windows!

## Features
* Opens the current folder or the root folder if `git init`
* Support context menu on sidebar's folder or file
* Title of the window with the project name and the path to the root folder (if `git init`)
* Launch type options for CMD or PowerShell, in a new window or tabs in the same window


## Installation
1º - You should install the CMDER from (http://cmder.net/) first, and add `ConEmu.exe` to the `%PATH%` environment var.

2º - Copy this project to the Sublime Text 3 Packages directory:

`C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\Packages\`

3º - Make sure the path to the `ConEmuOpen.py` file looks like this:

`C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\Packages\Sublime_ConEmuOpen\ConEmuOpen.py`


## Usage

* In sidebar menu of file or folder, use option "Open CMDER [ConEmu] Here"
* Use shortcuts with file already open, see keymap:
- `git init` needed to be considered root folder

CMD in new window [Root folder]
ctrl+1 OR ctrl+keypad1

CMD in new window [Current file folder]
ctrl+shift+1 OR ctrl+shift+keypad1

CMD in tabs [Root folder]
ctrl+2 OR ctrl+keypad2

CMD in tabs [Current file folder]
ctrl+shift+2 OR ctrl+shift+keypad2

PowerShell in new window [Root folder]
ctrl+3 OR ctrl+keypad3

PowerShell in new window [Current file folder]
ctrl+shift+3 OR ctrl+shift+keypad3

PowerShell in tabs [Root folder]
ctrl+4 OR ctrl+keypad4

PowerShell in tabs [Current file folder]
ctrl+shift+4 OR ctrl+shift+keypad4

Legacy version 1.3.0 - PowerShell in tabs [Current file folder]
alt+c 

Legacy version 1.3.0 - PowerShell in tabs [Root folder]
ctrl+alt+c


## License:

Licensed under MIT

Copyright (c) 2015 [kiliwalk](https://github.com/kiliwalk)
