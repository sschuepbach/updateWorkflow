import pyinotify

path = '/home/seb/temp/test/input'

wm = pyinotify.WatchManager()

notifier = pyinotify.Notifier(wm)

wm.add_watch(path, pyinotify.ALL_EVENTS)

# notifier.loop()
test = notifier.check_events()
print(test)
notifier.stop()