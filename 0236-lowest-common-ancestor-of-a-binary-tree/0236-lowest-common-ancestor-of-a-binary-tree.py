# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         self.anc = None
#         def dfs(node):
#             if node is None:
#                 return False
                        
#             left = dfs(node.left)
#             right = dfs(node.right)
#             cur = node == q or node == p
            
#             if cur + right + left == 2:
#                 self.anc = node
            
#             return left or right or cur
        
#         dfs(root)
#         return self.anc

        parent = {}
    
        def dfs(node,p):
            if node is None:
                return 
            parent[node] = p
            
            dfs(node.right,node)
            dfs(node.left,node)
            
        
        dfs(root,None)
        
        ancestors = set()
        ancestors.add(q)
        
        while q:
            ancestors.add(parent[q])
            q = parent[q]
        
        while p not in ancestors:
            p = parent[p]
        
        return p
        
        
            
            
            
                