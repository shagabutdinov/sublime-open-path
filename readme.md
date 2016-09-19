# Sublime OpenPath plugin

Open path in file browser by shortcut and provide API for other plugins to open
file browser in os-independent way. Based on [openfolder](https://github.com/mikepfirrmann/openfolder)
plugin so all cheers to original author.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

- Open project folder in file browser by hitting shortcut

- Open current file folder in file browser by hitting shortcut

- Providing open_path python module for external plugins


### Usage

Hit keyboard shortcut to open project or file folder. Map often-used opened
folders to your keymap file (command "open_path", {"path": "/home/leo"}).


### Commands

| Description         | Keyboard shortcuts | Command palette               |
|---------------------|--------------------|-------------------------------|
| Open project folder | f10                | OpenPath: Open project folder |
| Open file folder    | ctrl+f10           | OpenPath: Open file folder    |

## Customize shortcuts

Open preferences->key bindings->user and add your own shortcuts example:

	{"keys": ["alt+e"], "command": "open_file_folder"},
	{"keys": ["ctrl+alt+e"], "command": "open_project_folder"}

### Dependencies

None


### API

OpenPath.open_path:


##### open_path(path)

Opens given path in file manager.
