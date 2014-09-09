# Notifications

Sublime text plugin that uses terminal-notifier or subnotify for event notifications

## Installation
### Mac
###### Install terminal-notifier

```bash
gem install terminal-notifier
```

###### Install one of the following Sublime plugins
- [SubNotify](https://sublime.wbond.net/packages/SubNotify)
- [Terminal Notifier](https://sublime.wbond.net/packages/Terminal%20Notifier)

### Windows
1. Install the SubNotify plugin for Windows.
2. Install either of the following
	- [Growl for Windows](http://growlforwindows.com)
	- Install [Pywin32](https://sublime.wbond.net/packages/Pywin32)

The Pywin32 plugin allows standard windows notifications via the task bar while growl for Windows allows growl style notifications.

### Install this plugin
- Download repo directly into Packages folder
- Install via Package Control

###### Setup Preferences
Make sure Terminal Notifier or SubNotify are setup correctly.



Tell Notifications which plugin you want to use to display the notifications

```json
{
	"notifier": "subnotify"
}
```

__Note:__ SubNotify is currently the default because it supports multiplatform notifications.



### To Do:
- Enable custom message and title

Currently only post save notifications are setup. If you would like to see other notifications, please open a github issue and tag it as an enhancement.
