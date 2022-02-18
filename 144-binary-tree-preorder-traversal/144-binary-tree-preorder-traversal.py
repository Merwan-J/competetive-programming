# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        arr = []
        
        def helper(node):
            if node.right is None and node.left is None:
                arr.append(node.val)
                return None
            
            arr.append(node.val)
            
            if node.left:
                helper(node.left)
            
            if node.right:
                helper(node.right)
        helper(root)
        
        return arr