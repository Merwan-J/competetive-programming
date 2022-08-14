# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(list)
        nodes = set()
        
        for parent,child,isleft in descriptions:
            nodes.add(child)
            graph[parent] = graph.get(parent,[])+[-child if isleft else child]

        head = None
        for node in graph:
            if node not in nodes:
                head = node
                break

        def build(val):
            node = TreeNode(val)
            
            if graph[val]==[]:
                node.right = None
                node.left = None
                return node
            
            mn,mx = min(graph[val]),max(graph[val])
            
            left = build(-mn) if mn<0 else None
            right = build(mx) if mx>0 else None
            
            node.right,node.left = right,left
            
            return node
        
        return build(head)
            
            
            
            
            
                
        
            