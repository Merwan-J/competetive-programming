# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
#         def dfs(node,val):
#             if val>node.val:
#                 if node.right:
#                     return dfs(node.right,val)
#                 node.right = TreeNode(val)
#             else:
#                 if node.left:
#                     return dfs(node.left,val)
#                 node.left = TreeNode(val)
        
#         if root is None:
#             return TreeNode(val)
#         dfs(root,val)
#         return root

        if root is None:
            return TreeNode(val)
        
        node = root
        
        while node:
            if val>node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
        