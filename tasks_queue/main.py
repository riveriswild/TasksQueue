from task_queue import TaskQueue
from worker import Worker
from config import NUM_WORKERS


def main():
    task_queue = TaskQueue()

    workers = [Worker(task_queue) for _ in range(NUM_WORKERS)]

    for worker in workers:
        worker.start()

    # Example usage
    for i in range(10):
        task_queue.add_task(f"Task {i}")

    task_queue.join()

    for worker in workers:
        worker.stop()
        worker.join()


if __name__ == "__main__":
    main()
