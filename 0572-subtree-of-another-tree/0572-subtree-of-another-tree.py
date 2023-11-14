# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def check(p,q): 
            if p == q == None:
                return True 
            
            if not (p and q):
                return False
            
            if p.val != q.val:
                return False 
            
            return check(p.left,q.left) and check(p.right,q.right)
        
        
        def findNode(node):
            if node is None:
                return False
            
            ans = findNode(node.right) or findNode(node.left)
            
            if node.val == subRoot.val:
                ans = ans or check(node,subRoot)
            
            return ans  
        
        return findNode(root)