#using watchdog module to check
import watchdog.events
import watchdog.observers
import time
from watchdog.events import FileSystemEventHandler
import os

class FileWatcherBinding(watchdog.events.PatternMatchingEventHandler):
    #initial function
    def _init_(self,timee:int):
        """
        Default funciton to call watchdog module with correct parameters

        parameters being asked are  : timee : what is timee

        """
        self.timee = timee
        time.sleep(timee)
        watchdog.events.PatternMatchingEventHandler._init_(self, patterns=['*'],ignore_directories=False, case_sensitive=False)
   
    def on_any_event(self, event):
        #creating a log file
        f=open('log.txt','a')
        f.write("Watchdog received event happen- % s." % event.src_path+" . Event = "+event.event_type+"\n")
        f.close()
        print("Watchdog received event happen- % s." % event.src_path+" . Event = "+event.event_type+"\n")

    
    def file_event_hadler(self,path:str):
        abs_path = os.path.abspath(path)
        path_arr = abs_path.split('\\')
        abs_path = abs_path.replace(path_arr[len(path_arr)-1], '')
        self.start_watching(abs_path)
    
    def dir_event_handler(self,path:str):
        abs_path = os.path.abspath(path)
        self.start_watching(abs_path)
    
    def start_watching(self, dirname:str):
        event_handler = FileWatcherBinding(self.timee)
        FileSystemEventHandler.on_any_event = FileWatcherBinding.on_any_event
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, dirname, recursive=True)
        observer.start()
        print("Watching directory: " + dirname)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Terminated")
            observer.stop()
        observer.join()
