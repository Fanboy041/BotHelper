import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self, script_name):
        self.script_name = script_name
        self.observer = Observer()

    def run(self):
        event_handler = Handler(self.script_name)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = subprocess.Popen([sys.executable, self.script_name])

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            if event.src_path.endswith(".py"):
                print(f"{event.src_path} has been modified. Restarting script...")
                self.process.terminate()
                self.process = subprocess.Popen([sys.executable, self.script_name])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python watcher.py <script_to_watch>")
        sys.exit(1)
    script_to_watch = sys.argv[1]
    w = Watcher(script_to_watch)
    w.run()
