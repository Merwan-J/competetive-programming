# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        
        
        def dfs(node):
            if node is None:
                return -inf 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            curMax = max(node.val,left+node.val,right+node.val)
            
            self.ans = max(self.ans,left,right,left+right+node.val,curMax)
            
            return curMax
        
        dfs(root)
        
        return self.ans 
    