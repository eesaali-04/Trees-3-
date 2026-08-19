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
