# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def findMax(l,r):
            maxNum = max(nums[l:r+1])
            return nums.index(maxNum)
        
        def dfs(l,r):
            if r<l:
                return None 
            if l == r:
                return TreeNode(nums[l])
            
            maxIndex = findMax(l,r)
            
            root = TreeNode(nums[maxIndex])
            left = dfs(l,maxIndex-1)
            right = dfs(maxIndex+1,r)
            
            root.left = left
            root.right = right
            
            return root 
        
        return dfs(0,len(nums)-1)
        