# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            self.nodes.append(root)
            inorder(root.right)
        
        inorder(root)
        
        srt = sorted(node.val for node in self.nodes)
        
        for i in range(len(srt)):
            self.nodes[i].val = srt[i]
        