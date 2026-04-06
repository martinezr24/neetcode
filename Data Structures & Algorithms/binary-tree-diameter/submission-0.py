# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def depth(self, root):
            if not root:
                return 0
            
            left = depth(self, root.left)
            right = depth(self, root.right)

            self.maxD = max(left + right, self.maxD)

            return 1 + max(left, right)
        depth(self, root)
        return self.maxD




