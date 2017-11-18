import sublime
import sublime_plugin
import sublime_api

TITLE_ID = 0
PATH_ID = 1

class QuickFileOpenCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        if settings.has('menu'):
            menu = settings.get('menu')
            titles = [title[TITLE_ID] for title in menu]
            if type(titles) == list:
                self.window.show_quick_panel(titles, self.on_done)
            elif titles is None:
                self.window.show_quick_panel(['Set the \'menu\' setting to use QuickFileOpen'], None)
        else:
            sublime.error_message('The \'menu\' setting not found')

    def on_done(self, selected):
        if selected == -1:
            return
        settings = sublime.load_settings('QuickFileOpen.sublime-settings')
        file = settings.get('menu')[selected][PATH_ID]
        if(file != ''):
            self.window.open_file(file)
