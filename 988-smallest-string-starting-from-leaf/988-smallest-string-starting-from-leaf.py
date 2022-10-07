# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        path = deque([])
        def dfs(node):
            nonlocal ans
            if node is None:
                return
            
            path.appendleft(chr(node.val+ord('a')))
            
            if node.right == node.left == None:
                if ans is None: ans = "".join(path)
                else: ans = min(ans,"".join(path))

            dfs(node.right)
            dfs(node.left)
            path.popleft()
        
        dfs(root)
        return ans
        
