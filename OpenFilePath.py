import sublime_plugin, open_path

class OpenFileFolder( sublime_plugin.WindowCommand ):
  def run( self ):
    if self.window.active_view() is None:
      return

    open_path.open( os.path.dirname( self.window.active_view().file_name() ) )