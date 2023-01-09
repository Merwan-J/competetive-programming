# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         def dfs(node):
#             if node is None:
#                 return
            
#             self.ans.append(node.val)
#             dfs(node.left)
#             dfs(node.right)
            
#         self.ans = []
#         dfs(root)
        
#         return self.ans
    
        stack = []
        ans = []
        
        if root:
            stack.append(root)
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return ans
        
        
        
        