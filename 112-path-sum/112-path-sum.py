# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def visit(node,total):
            total+=node.val
            
            if node.right==node.left==None:
                return targetSum==total
            
            found = False
            
            if node.right:
                found =  visit(node.right,total)
            
            if found:
                return True
            
            if node.left:
                found = visit(node.left,total)
                
            return found
        
        return visit(root,0)
                
            