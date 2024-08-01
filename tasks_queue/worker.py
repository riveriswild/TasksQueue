import threading
import time
from task_queue import TaskQueue

class Worker(threading.Thread):
    def __init__(self, task_queue: TaskQueue):
        super().__init__()
        self.task_queue = task_queue
        self.running = True

    def run(self):
        while self.running:
            task = self.task_queue.get_task()
            if task:
                self.process_task(task)
                self.task_queue.task_done()
            else:
                time.sleep(1)

    def process_task(self, task):
        print(f"Processing task: {task}")
        time.sleep(2)  # Simulate task processing

    def stop(self):
        self.running = False
