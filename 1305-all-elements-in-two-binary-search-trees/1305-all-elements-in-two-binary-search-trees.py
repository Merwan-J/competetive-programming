# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node,arr):
            if node is None:
                return
            
            inorder(node.left,arr)
            arr.append(node.val)
            inorder(node.right,arr)
        
        n1 = collections.deque([])
        n2 = collections.deque([])
        
        inorder(root1,n1)
        inorder(root2,n2)
        
        
        
        
        return sorted(n1+n2)
            