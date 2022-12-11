# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val
            
            self.ans = max(self.ans,cur,cur+left,cur+right,cur+left+right)
            
            return max(cur,cur+left,cur+right)
        
        
        self.ans = -inf
        dfs(root)
        
        return self.ans
            
            
                        