# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node,target,seen):
            if node is None:
                return 
            
            target-=node.val
            seen.append(node.val)
            
            if node.right is None and node.left is None and target == 0:
                ans.append(seen.copy())
            
            dfs(node.right,target,seen)
            dfs(node.left,target,seen)
            seen.pop()
            
        dfs(root,targetSum,[])
        return ans
                