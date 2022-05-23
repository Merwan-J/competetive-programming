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
        LeftNodes = []
        RightNodes = []
        
        def right(node):
            if node is None:
                RightNodes.append(None)
                return 
            RightNodes.append(node.val)
            
            right(node.right)
            right(node.left)
        
        def left(node):
            if node is None:
                LeftNodes.append(None)
                return
            LeftNodes.append(node.val)
            
            left(node.left)
            left(node.right)
        
        right(root)
        left(root)
        return LeftNodes==RightNodes
        