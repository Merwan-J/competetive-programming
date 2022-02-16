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
        
        return handler(root,0)
        