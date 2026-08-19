class Tree:
    def __init__(self,root):
        self.root = root
        self.right = None
        self.left = None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.root, end = ' ')
        if self.right:
            self.right.inorder_traversal()

    def insert(self,key):
        if key < self.root:
            if self.left is None:
                self.left = Tree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key)
            else:
                self.right.insert(key)

    def inorder_predecessor(self): # Largest value smaller than key
        current = self.left
        while current and current.right:
            current = current.right
        return current
    
    def inorder_successor(self): # Smallest value greater than key
        current = self.right
        while current and current.left:
            current = current.left
        return current
    
    def delete(root,key):
        if root is None:
            return None
        if key < root.root:
            root.left = Tree.delete(root.left, key)
        elif key > root.root:
            root.right = Tree.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # If a node has 2 childeren get the inorder successor
            temp = root.inorder_successor()
            root.root = temp.root
            # Delete the inorder successor
            root.right = Tree.delete(root.right, temp.root)
        return root


root = Tree(11)
root.insert(9)
root.insert(3)
root.insert(16)
root.insert(2)
print('\nInorder traversal before deletion: ')
root.inorder_traversal()

print(f'\nInorder predecessor of 11 is {root.inorder_predecessor().root} ')
print(f'\nInorder successor of 11 is {root.inorder_successor().root}')
print('\nDeleting node 9')
root = Tree.delete(root, 9)
print('\nInorder traversal after deletion: ')
root.inorder_traversal()