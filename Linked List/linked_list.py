''' Implementing a singly linked list in python. 
    head -> |data|next| -> |data|next| -> |data|next| -> NULL
    Functions:
        Search - O(n)
        Insert - O(1)
        Deletion - O(1)
    Space complexity: O(n)
    Applications:
        Dynamic memory allocation
        Implemented in stacks and queues
        "undo" functionality 
        Hash tables, graphs
    Types:
        Single, Double, Circular
'''


class Node:
    ''' Create a node for the linked list. '''

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    ''' Create a new linked list data structure. '''

    def __init__(self) -> None:
        self.head = None

    def printList(self):
        ''' Print the linked list '''
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def insertFront(self, data):
        ''' Insert new node at the front of the list '''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        ''' Insert new node after a value prev_node '''
        if prev_node is None:
            print("Node not in linked list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertEnd(self, data):
        ''' Insert new node at the end of the list '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, position):
        ''' Delete a node after a given position '''

        # Empty list case
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        # One element in list case
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # find key to delete
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                print(f"Found element!")
                return True
            curr = curr.next
        return False

    def sort(self, head):
        curr = head
        index = Node(None)
        if head is None:
            return
        else:
            while curr is not None:
                index = curr.next
                while index is not None:
                    if curr.data > index.data:
                        curr.data, index.data = index.data, curr.data
                    index = index.next
                curr = curr.next


if __name__ == '__main__':

    ll = LinkedList()

    ll.insertFront(2)
    ll.insertFront(4)
    ll.insertEnd(9)
    ll.insertFront(6)
    ll.insertFront(7)
    ll.insertEnd(19)
    ll.insertFront(3)

    print("Initial LL:")
    ll.printList()

    print("After deletion:")
    ll.deleteNode(3)
    ll.printList()

    print("Sorted:")
    ll.sort(ll.head)
    ll.printList()
