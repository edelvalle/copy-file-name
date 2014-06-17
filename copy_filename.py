import sublime
import sublime_plugin
from os.path import basename


class FileNameNedded(sublime_plugin.TextCommand):
    def is_enabled(self):
        return bool(self.view.file_name())

    def send_to_clipboard(self, text, status_message=None):
        sublime.set_clipboard(text)
        sublime.status_message(status_message.format(text=text))


class CopyFilenameCommand(FileNameNedded):
    def run(self, edit):
        filename = basename(self.view.file_name())
        self.send_to_clipboard(filename, "Copied file name: {text}")


class CopyFilepathCommand(FileNameNedded):
    def run(self, edit):
        filepath = self.view.file_name()
        self.send_to_clipboard(filepath, "Copied file path: {text}")
