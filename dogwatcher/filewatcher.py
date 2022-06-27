#using WatchDog Module
import time
import watchdog.observers 
import watchdog.events 

#defining class to handle events
class FileWatcherBinding(watchdog.events.FileSystemEventHandler):
               #constructor
               def __init__(self,times,flag):
                 time.sleep(times)
                 #sets the patterns for PatternMatchingEventHandler
                 watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*'],ignore_directories=flag, case_sensitive=False)
                   
                #checking for creating events
               def on_created(self,event):
                  #creating a log file
                  f=open('watch_event.txt','a')
                  f.write("Created event -%s."%event.src_path)
                  f.close()
                  print("event created")

                #checking for modifing events
               def on_modified(self,event):
                #creating log file
                  f=open("watch_event.txt",'a')
                  f.write("modified event -%s."%event.src_path)
                  f.close()
                  print("modified event")

                #checking for deleting events
               def on_deleted(self,event):
                  f=open("watch_event.txt",'a')
                  f.write("deleted event -%s."%event.src_path)
                  f.close()
                  print("Deleted event- %s."%event.src_path)

                #checking for any event
               def on_any_event(self,event):
                  f=open("lwatch_event.txt",'a')
                  f.write("some event occured -%s."%event.src_path)
                  f.close()
                  print("som event occured")

                #checking moving event
               def on_moved(self,event):
                  f=open("watch_event.txt",'a')
                  f.write("moving event -%s."%event.src_path)
                  f.close()
                  print("moved event")

                #checking closed event 
               def on_closed(self,event):
                f=open("watch_event.txt")
                f.write("closed event -%s."%event.src_path)
                f.close()
                print("closed event")

                #function for file event handling
               def file_event_hadler(self,src_path):
                  observer =watchdog.observers.Observer();
                  observer.schedule(self,path=src_path,recursive=True)
                  observer.start()

                 #Exists on keyboard interrupt
                  try:
                    print("Monitoring")
                    while True:
                        pass
                  except KeyboardInterrupt:
                    print("exiting")
                    observer.stop()
                  observer.join()

                  #function for Directory event Handling
               def dir_event_handler(self,src_path):
                  observer =watchdog.observers.Observer();
                  observer.schedule(self,path=src_path,recursive=True)
                  observer.start()

                 #Exists on keyboard interrupt
                  try:
                    print("Monitoring")
                    while True:
                        pass
                  except KeyboardInterrupt:
                    print("exiting")
                    observer.stop()
                  observer.join()


if __name__ == "__main__":
    #choice to choose file or directory event handling
    # 1 for File Event Handling
    # 2 for Directory Event Handling 
    c=int(input("1.File Event Handling\n2.Directory Event Handling"))
    if c==1:
        print("enter file path")
    else:
        print("enter directory path")
    
    #getting path from user
    src_path=input()

    #making instance of class 
    #for file event handling pass True else pass false
    if c==1:
        event_handler=FileWatcherBinding(5,True)
        event_handler.file_event_hadler(src_path)
    else:
        event_handler=FileWatcherBinding(5,False)
        event_handler.dir_event_handler(src_path)
             
