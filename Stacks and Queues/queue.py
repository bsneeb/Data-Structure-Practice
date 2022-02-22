''' Implementing a basic queue in python. Queues are FIFO data structures. 
    Operations:
        Enqueue: Add element to queue
        Dequeue: remove element from queue
        O(1) function complexity
    Applications:
        CPU Scheduling
        IO Buffers
        Interrupt handling
        Call centers
'''


class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue.pop(0)

    def print(self):
        print(f"Queue: {self.queue}")

    def size(self):
        return len(self.queue)


if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(6)
    queue.enqueue(3)
    queue.enqueue(8)

    queue.print()

    queue.dequeue()

    queue.print()

    queue.enqueue(9)

    queue.print()
