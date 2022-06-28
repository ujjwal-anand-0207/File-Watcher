"""
using watchdog module
"""
import watchdog.events
import watchdog.observers
import time
from watchdog.events import FileSystemEventHandler
import os

class FileWatcherBinding(watchdog.events.PatternMatchingEventHandler):
    
    def _init_(self,timee:int):
        """
        Default funciton to call watchdog module with correct parameters

        parameters being asked are  : timee(int) : sampling frequency 

        """
        self.timee = timee
        time.sleep(timee)
        watchdog.events.PatternMatchingEventHandler._init_(self, patterns=['*'],ignore_directories=False, case_sensitive=False)
   
    def on_any_event(self, event):
        """
        Function to write in log file if any event occured 
        
        parameters being asked are : event : its a event which is on file
        """
        f=open('log.txt','a')
        f.write("Watchdog received event happen- % s." % event.src_path+" . Event = "+event.event_type+"\n")
        f.close()
        print("Watchdog received event happen- % s." % event.src_path+" . Event = "+event.event_type+"\n")

    
    def file_event_hadler(self,path:str):
        """
        function to accept path of file and call start_watching function for that file
        
        parameter asked are : path(string) : path of file on which events are to be monitored
        """
        abs_path = os.path.abspath(path)
        path_arr = abs_path.split('\\')
        abs_path = abs_path.replace(path_arr[len(path_arr)-1], '')
        self.start_watching(abs_path)
    
    def dir_event_handler(self,path:str):
         """
        function to accept path of directory and call start_watching function for that directory
        
        parameter asked are : path(string) : path of directory on which events are to be monitored
        """
        abs_path = os.path.abspath(path)
        self.start_watching(abs_path)
    
    def start_watching(self, dirname:str):
        """ 
        fuction for watchdog module to check event occured on file
        
        parameter asked are : dirname(string) : path of the directory/file
        """
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
