# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
#         LeftNodes = []
#         RightNodes = []
        
#         def right(node):
#             if node is None:
#                 RightNodes.append(None)
#                 return 
#             RightNodes.append(node.val)
            
#             right(node.right)
#             right(node.left)
        
#         def left(node):
#             if node is None:
#                 LeftNodes.append(None)
#                 return
#             LeftNodes.append(node.val)
            
#             left(node.left)
#             left(node.right)
        
#         right(root)
#         left(root)
#         return LeftNodes==RightNodes
        
        def isMirror(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            
            return node1.val==node2.val and isMirror(node1.left,node2.right) and isMirror(node1.right,node2.left)
        
        return isMirror(root,root)