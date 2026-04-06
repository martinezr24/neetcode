# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(self, p, q):
            if not p and not q: return True
            
            if not p and q: return False
            if p and not q: return False
            if p.val != q.val: return False
            
            left = sameTree(self, p.left, q.left)
            right = sameTree(self, p.right, q.right)

            return left and right
        
        if not subRoot: return True
        if not root: return False

        if sameTree(self, root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

