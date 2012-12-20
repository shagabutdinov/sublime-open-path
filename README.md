Sublime open file/project folder plugin.
========================================

Sublime open-by-shortcut file/project folder plugin. Based on https://github.com/mikepfirrmann/openfolder.


Features
--------

- Open project folder in explorer by hitting shortcut

- Open current file folder in explorer by hitting shortcut

- Providing open_path python module for external plugins


Configuration
-------------

This is my preferred configuration. Add it to your ".sublime-keymap" to start using the plugin.

    {
      "keys": ["f10"],
      "command": "open_project_folder"
    },

    {
      "keys": ["ctrl+f10"],
      "command": "open_file_folder"
    }


API usage
---------

    import open_path
    open_path.open( '/your/path/' ) # will open path in OS's file browser