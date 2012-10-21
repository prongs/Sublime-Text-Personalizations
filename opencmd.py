import sublime, sublime_plugin,os

class OpenCommandWindowHereCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print self.view.file_name()
		dire = os.path.dirname(self.view.file_name())
		command=' '.join(["cmd", "/c", '"cd', dire, '&&start"'])
		print command
		retcode = os.system(command)

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0
