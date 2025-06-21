# watch_folder.py
import time, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class PDFHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(patterns=["*.pdf"], ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print(f"[Watcher] New PDF added: {event.src_path}")
        os.system("python fill_db.py")

if __name__ == "__main__":
    path = "data"
    observer = Observer()
    observer.schedule(PDFHandler(), path=path, recursive=False)
    observer.start()
    print(f"Watching {path}/ for new PDFs...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
