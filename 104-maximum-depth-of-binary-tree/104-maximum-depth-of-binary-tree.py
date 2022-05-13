# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def handler(node,count):
            if node is None:
                return count
            
            left = handler(node.left,count+1)
            right = handler(node.right,count+1)
            
            return max(left,right)
#         def helper(node):
#             if node.right is None and node.left is None:
#                 return 1
            
#             right = helper(node.right) if node.right else 0
#             left = helper(node.left) if node.left else 0
            
#             return max(left,right)+1
        
#         return helper(root) if root else 0
        
        return handler(root,0)
        
