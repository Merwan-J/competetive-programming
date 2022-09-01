# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxx):
            if node is None:
                return 0
            ans = 0 if node.val <maxx else 1
            maxx = max(node.val,maxx)
            return ans + dfs(node.right,maxx) + dfs(node.left,maxx)
        
        return dfs(root,float('-inf'))