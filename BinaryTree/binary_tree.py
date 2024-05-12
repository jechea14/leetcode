from typing import Optional


class TreeNode:
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None


# #236 Invert Binary Tree
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # base case return to go up the tree
    if root is None:
        return

    # similar to swapping variables
    tmp: TreeNode = root.left
    root.left = root.right
    root.right = tmp

    # recursively call this function method for the left then right nodes
    invertTree(root.left)
    invertTree(root.right)

    # return the original root
    return root
