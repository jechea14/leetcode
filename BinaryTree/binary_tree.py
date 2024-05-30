from typing import List, Optional


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


# #572 Subtree of Another Tree
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # use solution from leetcode #100 same tree as helper function
    def isSameTree(root1, root2):
        # both nodes are null so true
        if root1 is None and root2 is None:
            return True
        # one node is null but the other isn't so not the same
        if root1 is None or root2 is None:
            return False
        # both node values are not the same
        if root1.val != root2.val:
            return False

        return isSameTree(root1.left, root2.left) and isSameTree(
            root1.right, root2.right
        )

    # check if root exists before comparing sub root
    if root is None:
        return False

    # use same tree function
    # returns true if it is same tree
    if isSameTree(root, subRoot):
        return True

    # recurse through left and right nodes to compare with sub root
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


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
            left_node.val == right_node.val
            and
            # split into left side
            dfs(left_node.left, right_node.right)
            and
            # split into right side
            dfs(left_node.right, right_node.left)
        )

    # call function and pass left and right nodes of the root
    return dfs(root.left, root.right)


# #617 Merge Two Binary Trees
def mergeTrees(
    root1: Optional[TreeNode], root2: Optional[TreeNode]
) -> Optional[TreeNode]:
    # recursive way

    # base case
    # if both nodes are null then return None
    if not root1 and not root2:
        return None

    # get the values of the nodes
    # assign value if node exists, assigns 0 if it doesn't
    # similar to the adding linked list nodes problem
    val1 = root1.val if root1 else 0
    val2 = root2.val if root2 else 0

    # create a new node with the summed values
    root = TreeNode(val1 + val2)

    # recurse through the result tree
    # left of root1 and root2, pass in None if it doesn't exist
    # right of root1 and root2, pass in None if it doesn't exist
    root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = mergeTrees(
        root1.right if root1 else None, root2.right if root2 else None
    )

    # return the resulting tree
    return root


# #102 Binary Tree Level Traversal, Time O(n) iterate through each node once, Space O(n) using lists as extra space
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # bfs: breadth first search
    # go down the tree by layer

    # return empty array if input is empty
    if root is None:
        return []

    # bfs
    queue = [root]
    result = []
    # while queue is not empty
    while queue:
        # temp array for each layer
        temp = []

        # loop through the queue length to append values by layer
        for _ in range(len(queue)):

            popped = queue.pop(0)
            if popped.left != None:
                queue.append(popped.left)

            if popped.right != None:
                queue.append(popped.right)
            # append popped node to temp list for layering
            temp.append(popped.val)

        # append layer to result
        result.append(temp)


# #1448 Count Good Nodes in Binary Tree.
# T: O(n), dfs visit all nodes once
# S: O(n) using extra memory for recursion
def goodNodes(root: TreeNode) -> int:
    count = 0
    maxVal = root.val

    def dfs(node, maxVal):
        # python thing to use the global variable
        nonlocal count

        # base case
        if node is None:
            return

        # if the current node value is greater than the max value,
        # compare the maxval
        # increment count of good nodes
        if node.val >= maxVal:
            maxVal = max(maxVal, node.val)
            count += 1

        # pre order traversal dfs for left node and right node
        dfs(node.left, maxVal)
        dfs(node.right, maxVal)

    # call the dfs helper function with the root and maxval inputs
    dfs(root, maxVal)
    return count


# #98 Validate Binary Search Tree
def isValidBST(root: Optional[TreeNode]) -> bool:
    min = float("-inf")
    max = float("inf")

    def recurse(root, min, max):
        # base cases
        if root is None:
            return True
        # return false if values do not satisfy bst rules
        if root.val <= min or root.val >= max:
            return False

        # both left and right sides of tree must be true to be a valid bst
        # pass in the min and max values to be compared when recursing
        # pass in the current node
        return recurse(root.left, min, root.val) and recurse(root.right, root.val, max)

    return recurse(root, min, max)


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
# print(isSameTree(node_1, node_4))
print(levelOrder(node1))
