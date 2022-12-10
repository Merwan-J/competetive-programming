# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def findSum(node):
            if node is None:
                return 0
            
            return node.val + findSum(node.right) + findSum(node.left)
        
        def dfs(node,totalSum):
            if node is None:
                return 0
            
            subTreeSum = node.val + dfs(node.left,totalSum) + dfs(node.right,totalSum)
            self.ans = max(self.ans,(totalSum-subTreeSum)*subTreeSum)
            
            return subTreeSum
        
        mod = 10**9 + 7
        self.ans = 0     
        totalSum = findSum(root)
        dfs(root,totalSum)
        
        return self.ans%mod
        