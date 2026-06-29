# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, mn, mx):
            if node.val > mn and node.val < mx:
                new_min = max(mn, node.val)
                new_max = min(mx, node.val)

                if node.left and node.right:
                    return dfs(node.left, mn, new_max) and dfs(node.right, new_min, mx)
                elif node.left:
                    return dfs(node.left, mn, new_max)
                elif node.right:
                    return dfs(node.right, new_min, mx)
                else:
                    return True
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))