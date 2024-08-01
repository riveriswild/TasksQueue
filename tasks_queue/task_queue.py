import queue
import threading

class TaskQueue:
    def __init__(self):
        self.tasks = queue.Queue()
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:
            self.tasks.put(task)
            print(f"Added task: {task}")

    def get_task(self):
        with self.lock:
            if not self.tasks.empty():
                task = self.tasks.get()
                print(f"Got task: {task}")
                return task
            return None

    def task_done(self):
        with self.lock:
            self.tasks.task_done()

    def join(self):
        self.tasks.join()