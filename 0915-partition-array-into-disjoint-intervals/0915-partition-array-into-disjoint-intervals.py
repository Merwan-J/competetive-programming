class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        rightMin = [inf]*n
        rightMin[-1] = nums[-1]
        
        for i in range(n-2,-1,-1):
            rightMin[i] = min(rightMin[i+1],nums[i])
        
        curMax = nums[0]
        for i in range(n-1):
            curMax = max(nums[i],curMax)
            
            if curMax<=rightMin[i+1]:
                return i+1
        
