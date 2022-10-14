# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete(node,k):
            if node is None:
                return None
            
            if node.val == k:
                if node.right is None and node.left is None: return None
                if node.right and not node.left: return node.right
                if node.left and not node.right: return node.left
                
                toBeInserted = node.left
                rootToBe = node.right
                
                node = node.right
                
                while node.left:
                    node = node.left
                node.left = toBeInserted
                
                return rootToBe
                
            elif node.val<k:
                node.right = delete(node.right,k)
            else:
                node.left = delete(node.left,k)
            
            return node
        
        return delete(root,key)
        
        
        
       