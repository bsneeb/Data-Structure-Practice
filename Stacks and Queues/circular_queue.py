''' Implementing a circular queue in python. This eliminates the empty 
    space found in the basic queue after several enqueue and dequeue operations.
    This works by setting a max space value k to prevent overflow of address space
    Applications:
        CPU Scheduling
        Memory management
        traffic management
'''


class CircularQueue:

    def __init__(self, k) -> None:
        self.k = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enqueue(self, item):

        # Full queue special case
        if ((self.tail + 1) % self.k == self.head):
            print("Circular queue is full - can not enqueue")

        # Empty queue special case
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = item

    def dequeue(self):

        # No element special case
        if (self.head == -1):
            print("Nothing to dequeue - circular queue is empty")

        # One element special case
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def print(self):

        # No element special case
        if (self.head == -1):
            print("Circular queue is empty.")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")
            print()

        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == '__main__':

    # create a cq of size 6
    cq = CircularQueue(6)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)

    cq.print()

    cq.enqueue(7)

    cq.print()

    cq.dequeue()
    cq.dequeue()
    cq.dequeue()

    cq.print()

    cq.dequeue()
    cq.dequeue()
    cq.dequeue()

    cq.print()
