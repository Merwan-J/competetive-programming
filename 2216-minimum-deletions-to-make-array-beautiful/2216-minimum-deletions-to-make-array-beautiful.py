class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deleted = 0
        n = len(nums)
        
        for i in range(n):
            if (i-deleted)%2==0 and i+1<n and nums[i] == nums[i+1]:
                deleted += 1
        
        return deleted if (n-deleted)%2==0 else deleted + 1