# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        psum = defaultdict(int)
        psum[0]+=1
        
        self.count = 0
        
        def dfs(node,total):
            if node is None:
                return 0
            
            total+=node.val
            
            if total-target in psum:
                self.count+=psum[total-target]
            
            psum[total]+=1
            
            dfs(node.left,total)
            dfs(node.right,total)
            
            psum[total]-=1
            
        dfs(root,0)
        
        return self.count
            
        
        
        