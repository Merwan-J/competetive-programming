# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def dfs(node,k):
            nonlocal count,ans
            if node is None:
                return
            
            dfs(node.left,k)
            count+=1
            if count == k:
                ans = node
            dfs(node.right,k)            
        
        dfs(root,k)
        return ans.val