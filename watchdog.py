import time
import os
import shutil
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

source = "C:/Users/mahaj/Downloads"
dirtree={
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        name,exd=os.path.splitext(event.src_path)
        time.sleep(1)
        for i,value in dirtree.items():
            time.sleep(1)
            if exd in value:
                filename=os.path.basename(event.src_path)
                print("Downloaded "+filename)
                path1=source+"/"+filename
                path2=source+"/"+i
                path3=source+"/"+i+"/"+filename
                if os.path.exists(path2):
                    print("Moving the file ...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Making the folder")
                    os.makedirs(path2)
                    print("Moving the file ...")
                    shutil.move(path1,path3)
                    time.sleep(1)


event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler, source, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running ...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
    