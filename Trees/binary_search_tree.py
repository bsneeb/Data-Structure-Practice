''' Implementing a Binary Search Tree in python. This data structure
    allows for quick maintance on a sorted list of numbers. Each node
    has a maximum of two children.
    Search Time- O(log(n))
    Properties:
        All nodes in the left are less than root node
        All nodes in the right are more than the root node
    Complexity:
        Search: O(log(n))
        Insertion: O(log(n))
        Delete: O(log(n))
        Space: O(n)
    Applications:
        Multilevel indexing in database
        Dynamic sorting
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.key) + "->", end='')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValue(node):
    curr = node
    while(curr.left is not None):
        curr = curr.left
    return curr

def deleteNode(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValue(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

if __name__ == '__main__':
    
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=' ')
    inorder(root)

    print("\nDelete 10")
    root = deleteNode(root, 10)
    print("Inorder traversal: ", end=' ')
    inorder(root)
    