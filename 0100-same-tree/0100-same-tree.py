# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def check(p,q): 
            if p == q == None:
                return True 
            
            if not (p and q):
                return False
            
            if p.val != q.val:
                return False 
            
            return check(p.left,q.left) and check(p.right,q.right)
        
        return check(p,q)