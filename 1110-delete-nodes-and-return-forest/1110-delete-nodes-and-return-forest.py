# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        order = []
        def removeEdge(node,parent):
            if node is None:
                return 
            if node.val in to_delete:
                if node == parent.right:
                    parent.right = None
                else:
                    parent.left = None
            else:
                order.append(node)
                
            removeEdge(node.right,node)
            removeEdge(node.left,node)
            
        def visit(node,visited):
            if node is None:
                return 
            visited.add(node)
            
            visit(node.right,visited)
            visit(node.left,visited)
            
        removeEdge(root,TreeNode())
        
        visited = set()
        ans = []
        for node in order:
            if node not in visited:
                ans.append(node)
                visit(node,visited)
        return ans
                
            