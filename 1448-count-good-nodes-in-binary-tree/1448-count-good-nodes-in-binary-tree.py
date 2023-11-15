# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,pathMax):
            if node is None:
                return 0 
            
            curMax = max(pathMax,node.val)
            ans = dfs(node.right,curMax) + dfs(node.left,curMax)
            
            if node.val == curMax: ans+=1
            
            return ans 
        
        return dfs(root,root.val)