# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
            if l>r:
                return None
            mid = l+(r-l)//2
            node = TreeNode(nums[mid])
            node.right = helper(mid+1,r)
            node.left = helper(l,mid-1)
            
            return node
        
        return helper(0,len(nums)-1)