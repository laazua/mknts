### threading.Thread

- **多线程**
```python
import time
import queue
import threading


class TaskProducer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            task = {"id": i}
            print(f"producer: {task}")
            self.queue.put(task)
        self.queue.put(None)
        print("producer finished, sent signal")


class TaskConsumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            if task is None:
                print("consumer received stop signal")
                break
            print(f"consumer: {task}")
            time.sleep(1.5)


if __name__ == "__main__":
    q = queue.Queue(maxsize=5)
    producer = TaskProducer(q)
    consumer = TaskConsumer(q)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("===========================")

```