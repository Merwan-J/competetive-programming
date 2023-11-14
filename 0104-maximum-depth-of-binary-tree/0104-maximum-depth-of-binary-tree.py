# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if node is None:
                return 0 
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            return 1 + max(right,left)
        
        return dfs(root)