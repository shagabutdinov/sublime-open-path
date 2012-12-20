import sublime_plugin, open_path

class OpenProjectFolder( sublime_plugin.WindowCommand ):
  def run( self ):
    open_path.open( self.window.folders()[0] )