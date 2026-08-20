'''Delete a Node with One Child
Task: Create a function to delete a node that has exactly one child.
Input: A BST rooted at root and a target key.
Goal: Tree: 10 -> Right: 20 -> Right: 30. Delete(20). Output: 10 -> Right: 30.
Logic (Give If Needed):
Find the target node.
Check if it has only a left child (root.right is None) OR only a right child (root.left is None).
If only left: return root.left. (The parent will now point to the grandchild).
If only right: return root.right.'''

class Tree():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def delete(root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = Tree.delete(root.left, key)

        elif key > root.value:
            root.right = Tree.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
        return root


root = Tree(10)
root.right = Tree(20)
print('\nInorder traversal before deletion.')
root.inorder_traversal()
root = Tree.delete(root,20)
print('\nInorder traversal after deletion.')
root.inorder_traversal()

    