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


# #104 Maximum Depth of Binary Tree
def maxDepth(root: Optional[TreeNode]) -> int:
    # basecase check if root is empty
    if root is None:
        return 0

    depth: int = 0
    # bfs: use a queue and pop the beginning
    queue = [root]
    while queue:
        # use a for loop to iterate through the node of each level
        for i in range(len(queue)):
            node: TreeNode = queue.pop(0)
            # add the nodes to the queue
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        # increment the level
        depth += 1
    return depth


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

print(maxDepth(node1))
