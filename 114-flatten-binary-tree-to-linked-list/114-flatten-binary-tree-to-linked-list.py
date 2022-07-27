# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        
       
        
        """
        
        
        def dfs(node,parent):
            if node is None:
                return parent
            
            parent.left = None
            parent.right = node
            
            tempR = node.right
            
            left = dfs(node.left,node)
            right = dfs(tempR,left)
            
            return right
    
        dummy = TreeNode()
        dfs(root,dummy)
        
        
        