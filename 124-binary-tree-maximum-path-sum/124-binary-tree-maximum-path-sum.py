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
            
            if node.right == node.left == None:
                self.ans = max(self.ans,node.val)
                return node.val
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            self.ans = max(node.val,node.val+right+left,node.val+left,node.val+right,self.ans)
            
            return max(node.val,node.val+right,node.val+left)
        
        dfs(root)
        return self.ans
            
            
                        