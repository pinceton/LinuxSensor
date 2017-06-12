'''
Created on Jun 8, 2017

@author: gevans
'''

import pyinotify

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        print "File has been accessed:", event.pathname
    def process_IN_MODIFY(self, event):
        print "File has been modified:", event.pathname
    def process_IN_OPEN(self, event):
        print "File has been opened:", event.pathname

def main():
    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch('/var/log', pyinotify.ALL_EVENTS, rec=True)

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()