class Node:
    ''' Node object for search tree '''

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        ''' Prints all of the nodes in the binary search tree '''
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        ''' Insert a node into the binary search tree'''
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, val):
        ''' Finds a value in the BST '''
        if val < self.data:
            if self.left is None:
                return str(val) + " is not in tree"
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " is not in tree"
            return self.right.find(val)
        else:
            return "found value: " + str(val)


root = Node(10)
root.insert(2)
root.insert(92)
root.insert(66)
root.insert(20)
root.PrintTree()
print(root.find(22222))
