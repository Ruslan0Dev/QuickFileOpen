import sublime
import sublime_plugin
import sublime_api

class QuickFileOpenCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        index = '0'
        titles = []
        while settings.has(index):
            titles += [settings.get(index)[0]]
            index = str(int(index) + 1)
        if type(titles) == list:
            self.window.show_quick_panel(titles, self.on_done)
        elif item is None:
            self.window.show_quick_panel(['Set the \'items\' setting to use QuickFileOpen'], None)
        else:
            sublime.error_message('The \'items\' setting must be a list')

    def on_done(self, selected):
        if selected == -1:
            return
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        file = settings.get(str(selected))[1]
        if(file != ''):
            self.window.open_file(file)
