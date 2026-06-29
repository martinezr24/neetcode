# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node, highest):
            nonlocal good_nodes
            if node.val >= highest:
                good_nodes += 1
                highest = node.val
            if node.left:
                dfs(node.left, highest)
            if node.right:
                dfs(node.right, highest)

        dfs(root, root.val)
        return good_nodes