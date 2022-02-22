''' Implementing a full binary tree in python. A full binary tree
    has parent nodes with two or no children.
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def isFull(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isFull(root.left) and isFull(root.right))

    return False


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    # root.right.right = Node(7)

    if isFull(root):
        print("The tree is a full binary tree")
    else:
        print("The tree is not a full binary tree")
