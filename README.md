#Notifications

Sublime text plugin that uses terminal-notifier or subnotify for event notifications

##Installation
###Mac
######Install terminal-notifier

```bash
gem install terminal-notifier
```

######Install one of the following Sublime plugins
- Terminal Notifier
- SubNotify

######Install this plugin
- Download repo directly into Packages folder
- Install via Package Control

######Setup Preferences
Make sure Terminal Notifier or SubNotify are setup correctly.

Tell Notifications which plugin you want to use to display the notifications

```json
{
	"notifier": "subnotify"
}
```

__Note:__ SubNotify is currently the default because it supports multiplatform notifications. This plugin has not yet been verified to work with Windows but the plan is to support Windows in the future.
