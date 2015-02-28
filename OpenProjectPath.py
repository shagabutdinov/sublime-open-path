from OpenPath import open_path
import sublime_plugin

class OpenProjectFolder( sublime_plugin.WindowCommand ):
  def run( self ):
    open_path.open_path( self.window.folders()[0] )