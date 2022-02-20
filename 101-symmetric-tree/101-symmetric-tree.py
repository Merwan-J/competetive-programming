# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(root.left,root.right)
        arr1 = []
        arr2 = []
        
        def right(node):
            if node is None:
                arr2.append(None)
                return None
            
            if node.right is None and node.left is None:
                arr2.append(node.val)
                return None
            arr2.append(node.val)
            
            if node.right:
                right(node.right)
            else:
                arr2.append(None)
            
            if node.left:
                right(node.left)
            else:
                arr2.append(None)
            
           
        
        def left(node):
            if node is None:
                arr1.append(None)
                return None
            if node.right is None and node.left is None:
                arr1.append(node.val)
                return None
            arr1.append(node.val)
            if node.left:
                left(node.left)
            else:
                arr1.append(None)
            
            if node.right:
                left(node.right)
            else:
                arr1.append(None)
        
        right(root.right)
        left(root.left)
        return arr1==arr2
        