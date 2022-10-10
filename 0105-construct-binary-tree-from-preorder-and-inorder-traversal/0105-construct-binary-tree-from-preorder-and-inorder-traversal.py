# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        def dfs(inord):
            if not inord:
                return
            
            val = self.preorder[0]
            self.preorder = self.preorder[1:]
            
            mid = inord.index(val)
            left = dfs(inord[:mid])
            right = dfs(inord[mid+1:])
            
            return TreeNode(val, left, right)
        
        return dfs(inorder)