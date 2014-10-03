import sublime, sublime_plugin, os
from subprocess import call

def open_path(folder):
  settings = sublime.load_settings("OpenPath.sublime-settings")
  file_manager = settings.get("file_manager", "explorer /e /root,\"{0}\"")
  command = file_manager.format(folder)
  call(command, shell=True)

class OpenPath(sublime_plugin.WindowCommand):
  def run(self, path):
    open_path(path)

class OpenProjectFolder(sublime_plugin.WindowCommand):
  def run(self):
    if len(self.window.folders()) == 0:
      return

    open_path(self.window.folders()[0])

class OpenFileFolder(sublime_plugin.WindowCommand):
  def run(self):
    if self.window.active_view() is None:
      return

    open_path(os.path.dirname(self.window.active_view().file_name()))