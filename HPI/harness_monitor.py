import threading
import time
from Queue import Queue
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from harness_parser import *

dir_to_monitor = raw_input("Please enter directory to monitor : ")
class NewFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.q = Queue()
        self.thread = None
        self.harness_parse_lock=None

    def on_created(self,event):
        if not event.is_directory:
            self.q.put((event,dt.datetime.now()))

    def start(self):
        self.harness_parse_lock = threading.Lock()
        for x in range(5):
            self.thread = threading.Thread(target=self.process)
            self.thread.daemon=True
            self.thread.start()

    def process(self):
        while True:
            evnt , ts = self.q.get()
            file_path = evnt.src_path
            with self.harness_parse_lock:
                print "thread processing :" , threading.current_thread().name , file_path
                harness_parser(filename=file_path,create_time=ts)
            self.q.task_done()

def watch_dir():
    dir_observer = Observer()
    file_handler = NewFileHandler()

    file_handler.start()
    dir_observer.schedule(file_handler,path=dir_to_monitor,recursive=True)
    dir_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        dir_observer.stop()

    dir_observer.join()

if __name__ == '__main__':
    watch_dir()