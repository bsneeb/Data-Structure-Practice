''' Implementing a tree data structure in Python. Trees are nonlinear heirachical data
    structures that consist of nodes connected by edges. Treees allow for quicker access
    to data over linked lists and arrays. 

    Implementing tree traversals in python. Preorder, postorder and inorder.
    
'''


class Node:
    def __init__(self, item) -> None:
        self.left = None
        self.right = None
        self.val = item


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"{str(root.val)} ->", end="")


def preorder(root):
    if root:
        print(f"{str(root.val)} ->", end="")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(f"{str(root.val)} ->", end="")
        inorder(root.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal: ")
    inorder(root)

    print("\nPostorder: ")
    postorder(root)

    print("\nPreorder:")
    preorder(root)
