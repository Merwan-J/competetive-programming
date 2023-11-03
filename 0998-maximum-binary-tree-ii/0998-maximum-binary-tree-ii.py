# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.found = False
        def dfs(node):
            if node is None or node.val<val:
                self.found = True
                return TreeNode(val,node)
            
            right = dfs(node.right)
            left = node.left if self.found else dfs(node.left)
            
            node.right = right
            node.left = left
            
            return node 
        
        return dfs(root)