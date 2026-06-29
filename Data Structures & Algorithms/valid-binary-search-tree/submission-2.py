# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, ran):
            if node.val > ran[0] and node.val < ran[1]:
                mn = max(ran[0], node.val)
                mx = min(ran[1], node.val)

                if node.left and node.right:
                    return dfs(node.left, [ran[0], mx]) and dfs(node.right, [mn, ran[1]])
                elif node.left:
                    return dfs(node.left, [ran[0], mx])
                elif node.right:
                    return dfs(node.right, [mn, ran[1]])
                else:
                    return True
            else:
                return False

        return dfs(root, [float('-inf'), float('inf')])