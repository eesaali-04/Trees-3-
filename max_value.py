'''Find the Maximum Value in a BST
Task: Create a function to find the largest number in a Binary Search Tree.
Input: A BST rooted at root.
Goal: Output: The largest number in the tree.
Logic (Give If Needed):
In a BST, the largest value is always in the rightmost node.
Loop: While root.right is not None, move root to root.right.
Return root.data.'''

class Tree:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()


root = Tree(17)  
root.right = Tree(19)
root.left = Tree(13)
root.left.left = Tree(5)
root.left.right = Tree(7)

def max_value(root):
    if root is None:
        return root
    while root.right is not None:
        root = root.right
    return root.data

    
root.inorder_traversal()
print(f'The biggest value in the BST is {max_value(root)}')