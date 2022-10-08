# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            if node.right == node.left == None:
                return 1
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            if node.right and node.left and node.right.val == node.left.val == node.val:
                self.ans = max(self.ans,left+right+1)
                return max(left+1,right+1)
            elif node.right and node.right.val == node.val:
                self.ans = max(self.ans,right+1)
                return right+1
            elif node.left and node.left.val == node.val:
                self.ans = max(self.ans,left+1)
                return left+1
            
            return 1
        
        dfs(root)
        return self.ans-1 if self.ans>0 else 0
            
            