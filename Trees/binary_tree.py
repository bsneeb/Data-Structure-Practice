''' Implementing a binary tree in python. Binary trees have parent
    nodes with at most two children. Each node contains:
        A data item
        address to left child
        address to right child 
    Applications:
        Quick and easy access to data
        syntax tree   
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(f"{str(self.val)} ->", end="")

    def preorder(self):
        print(f"{str(self.val)} ->", end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(f"{str(self.val)} ->", end="")
        if self.right:
            self.right.inorder()


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal: ")
    root.inorder()

    print("\nPostorder: ")
    root.postorder()

    print("\nPreorder:")
    root.preorder()
