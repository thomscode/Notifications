import os
import subprocess
import sublime
import sublime_plugin

PLUGIN_SETTINGS = "notifications.sublime-settings"


class Notifiers(sublime_plugin.EventListener):
	""" Notify user on file save """
	def growl(self, msg, title):
		settings = sublime.load_settings(PLUGIN_SETTINGS)
		notifier = settings.get('notifier')

		if notifier == 'subnotify':
			# SubNotify
			sublime.active_window().run_command('sub_notify', {
				'title': title,
				'msg': msg,
				'sound': False
			})

		elif notifier == 'terminal-notifier':
			# Terminal Notifier
			sublime.active_window().run_command('terminal_notifier', {
				'title': title,
				# 'subtitle': title,
				'message': msg
			})

	def on_post_save(self, view):
		filename = os.path.basename(view.file_name())
		title = 'File was saved.'
		self.growl(filename, title)


print(os.getcwd())
