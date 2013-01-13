import sublime_plugin
import os
import webbrowser
import urllib


class OpenCommandWindowHereCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        dire = os.path.dirname(self.view.file_name())
        command = ' '.join(["cmd", "/c", '"cd', dire, '&&start"'])
        os.system(command)

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0


class SearchWithGoogle(sublime_plugin.TextCommand):
    def is_enabled(self):
        return any(not s.empty() for s in self.view.sel())

    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                continue
            url = "http://www.google.com/search?" + urllib.urlencode({"q": self.view.substr(s)})
            webbrowser.open(url)
