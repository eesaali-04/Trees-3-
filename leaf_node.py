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



root = Tree(9)
root.inorder_traversal()
root = Tree.delete(root, 9)
print('\n',root)