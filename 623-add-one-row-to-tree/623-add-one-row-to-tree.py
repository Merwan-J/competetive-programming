# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)
        
        def dfs(node,k):
            if node is None:
                return
            
            right = node.right
            left = node.left
            
            if k==1:
                new_right = TreeNode(val,None,right)
                new_left = TreeNode(val,left,None)
                
                node.right = new_right
                node.left = new_left
                
            else:
                dfs(node.right,k-1)
                dfs(node.left,k-1)
        
        dfs(root,depth-1)
        return root
        
        
        