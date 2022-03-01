''' AVL Tree
    This is a self balancing binary tree where each node maintains
    an extra value called the balance factor whose value is either
    1, 0 or -1. 
    Balance factor = (height of left subtree - height of right subtree)
    Complexities:
        Insertion:  O(log(n))
        Deletion:  O(log(n))
        Search:  O(log(n))
    Applicaitons:
        Indexing large records in a database
        Searching large databases
'''

import sys

class TreeNode(object):
    def __init__(self, key) -> None:
        self.key = key
        self.right = None
        self.left = None
        self.height = 1

class AVLTree(object):
    
    # Insert a node
    def insert_node(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:    
            root.right = self.insert_node(root.right, key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Balance the tree
        balance_factor = self.getBalance(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance_factor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    # Delete a node
    def delete_node(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance_factor = self.getBalance(root)

        # Balance tree
        if balance_factor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance_factor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.leftRotate(root.right)
                return self.leftRotate(root)

        return root

    # Perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Get height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def printTree(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printTree(currPtr.left, indent, False)
            self.printTree(currPtr.right, indent, True)

if __name__ == "__main__":
    
    tree = AVLTree()
    root = None
    nums = [33, 17, 54, 9, 21, 61, 8, 11]

    for num in nums:
        root = tree.insert_node(root, num)
    tree.printTree(root, "", True)
    key = 13
    root = tree.delete_node(root, key)
    print("After deletion: ")
    tree.printTree(root, "", True)

