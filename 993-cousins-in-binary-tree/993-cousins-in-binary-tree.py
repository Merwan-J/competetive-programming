# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xx = (0,0)
        self.yy = (0,0)
        
        def dfs(node,depth,parent):
            if node is None:
                return 
            depth += 1
            
            if node.val == x:
                self.xx = (depth,parent)
            elif node.val == y:
                self.yy = (depth,parent)
            
            dfs(node.right,depth,node)
            dfs(node.left,depth,node)
        
        dfs(root,0,None)
        return self.xx[0] == self.yy[0] and self.xx[1]!= self.yy[1]
        