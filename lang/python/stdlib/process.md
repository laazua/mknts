### 

- **多进程**
```python
import time
import multiprocessing


class TaskProducer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        
    def run(self):
        for i in range(10):
            task = {"id": i}
            print("producer: ", task)
            self.queue.put(task)
        # Add a special "None" task to signal the consumer to stop
        self.queue.put(None)
        print("producer finished, sent signal")


class TaskConsumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            if task is None:  # If the task is None, stop the consumer
                print("consumer received stop signal")
                break
            print("consumer: ", task)
            time.sleep(1)


if __name__ == "__main__":
    queue = multiprocessing.Queue(maxsize=5)
    producer = TaskProducer(queue=queue)
    consumer = TaskConsumer(queue=queue)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

    print("=====================")
```