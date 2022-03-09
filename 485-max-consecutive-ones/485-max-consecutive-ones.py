class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if  sum==sum-nums[i]:
                count = max(count,sum)
                sum = 0
            else:
                count = max(count,sum)
        return count