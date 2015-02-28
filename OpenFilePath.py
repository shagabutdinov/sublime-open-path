from OpenPath import open_path
import sublime_plugin, os

class OpenFileFolder( sublime_plugin.WindowCommand ):
  def run( self ):
    if self.window.active_view() is None:
      return

    open_path.open_path( os.path.dirname( self.window.active_view().file_name() ) )