# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        parent = defaultdict(TreeNode)
        
        def buildGraph(node,parentNode):
            if node is None:
                return 
            
            parent[node] = parentNode
            
            buildGraph(node.right,node)
            buildGraph(node.left,node)
            
        
        buildGraph(root,None)
        
        qPath = set()
        while q:
            qPath.add(q)
            q = parent[q]
        
        while p not in qPath:
            p = parent[p]
        
        return p 
        
            