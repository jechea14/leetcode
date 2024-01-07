# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()
        print(self.val)

    def preorder_traversal(self):
        print(self.val)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.val)

    def invertTree(self, root):
        if root is None:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root


tree = TreeNode(4)

tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)

print(tree.invertTree(tree))
tree.preorder_traversal()
