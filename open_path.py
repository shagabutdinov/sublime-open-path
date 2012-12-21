import sublime
from subprocess import call

def open( folder ):
  settings = sublime.load_settings( "OpenPath.sublime-settings" )
  file_manager = settings.get("file_manager", "explorer /e /root,\"{0}\"")
  command = file_manager.format( folder )
  call( command, shell=True )