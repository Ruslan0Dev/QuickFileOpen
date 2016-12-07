import sublime
import sublime_plugin
import sys, os

class QuickFileOpenCommand(sublime_plugin.WindowCommand):

  SETTING_PATH = 'QuickFileOpen.sublime-settings'
  data = []

  def run(self):
    self.data = sublime.load_settings(self.SETTING_PATH).get('item')
    items = self._get_content(self.data)

    self.show_panel(items)

  #  get one hierarchy item
  def _get_content(self, items):
    ret = []
    for item in items:

      if type(item['path']) == list:
        name = "[D] " + item['name']
        tmp = [ x['name'] for x in item['path'] ]
        path = ", ".join(tmp)
      else:
        name = item['name']
        path = item['path']

      ret.append([ name, path ])
    return ret

  def show_panel(self, items):

    if type(items) == list:
      self.window.show_quick_panel(items, self.on_done)
    elif items is None:
      self.window.show_quick_panel(["Set the 'files' setting to use QuickFileOpen"], None)
    else:
      sublime.error_message("The 'files' setting must be a list")


  def on_done(self, idx):
    if idx == -1:
      return

    # get recursive contents
    if type(self.data[idx]['path']) == list:

      self.data = self.data[idx]['path']
      items = self._get_content(self.data)
      self.show_panel(items)
    
    # get normal path
    else:
      filepath = self.data[idx]['path']
      if not os.path.exists(filepath):
        return

      self.window.open_file(filepath)
