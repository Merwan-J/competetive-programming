# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node is None:
                return None
            
            node.right,node.left = node.left,node.right
            
            helper(node.right)
            helper(node.left)
        helper(root)
        return root
        