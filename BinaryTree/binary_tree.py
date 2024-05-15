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
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        # increment the level
        depth += 1
    return depth


# #100 Same Tree
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # base cases, when both are None, when 1 or the other is None
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    # if the values are not equal to each other
    if p.val != q.val:
        return False
    # dfs, recursively want to return if both left and right sides satisfy
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# #543 Diameter of Binary Tree
# Time O(n), Space O(n)
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    # global variable to keep track of max depth
    max_depth: int = 0

    # depth first search (post order), start from the bottom
    # function created to keep global max_depth from getting messed up from recursion
    def dfs(rt: Optional[TreeNode]):
        # python thing, refers to the outer max_depth
        nonlocal max_depth
        # returns 0 when node is none
        if rt is None:
            return 0
        # put into variables to be used to get the sum of depths from both sides
        left: int = dfs(rt.left)
        right: int = dfs(rt.right)
        current_depth: int = left + right
        # compares current depth with max depth
        max_depth = max(current_depth, max_depth)
        # function returns the max depth of both sides and add 1 because going up a path counts as 1
        return max(left, right) + 1

    # call the dfs function
    dfs(root)
    return max_depth


# #101 Symmetric Tree. Time O(n), Space O(n)
def isSymmetric(root: Optional[TreeNode]) -> bool:
    # inner function because need left and right inputs for left and right nodes
    # dfs
    def dfs(left_node: TreeNode, right_node: TreeNode) -> bool:
        # base cases
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False

        return (
                # values must be equal
                left_node.val == right_node.val and
                # split into left side
                dfs(left_node.left, right_node.right) and
                # split into right side
                dfs(left_node.right, right_node.left)
        )
    # call function and pass left and right nodes of the root
    return dfs(root.left, root.right)


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(1)
node_4 = TreeNode(1)
node_5 = TreeNode(1)
node_6 = TreeNode(2)

node_1.left = node_2
node_1.right = node_3
node_4.left = node_5
node_4.right = node_6

# print(maxDepth(node1))
print(isSameTree(node_1, node_4))
