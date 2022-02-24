''' Hash table implementation in Python. Hash tables store elements
    in key-value pairs where:
        Key - unique int that is used for indexing the values
        Value - data that is associated with keys

    Solve collision in 2 ways:
        Chaining:
            If there is a collision, add that value to the same index through
            doubly linked list.
        Open Addressing:
            If there is a collision, find a new slot on the hash table using a
            technique of your choice. Options include: Linear Probing, Quadratic
            Probing, Double Hashing, Division, Multiplication or Universal Hashing

'''


INITIAL_CAPACITY = 10


class Node:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self) -> None:
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        for i, c in enumerate(key):
            hashsum += (i + len(key)) ** ord(c)

            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result


if __name__ == '__main__':

    ht = HashTable()
    nums = ["123", "456", "789"]
    ht.insert("Numbers", nums)
    nums = None

    nums = ht.find("Numbers")
