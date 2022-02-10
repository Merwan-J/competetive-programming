class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#   Brute-Force
        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     crntSum = 0
        #     for j in range(i,len(nums)):
        #         crntSum+=nums[j]
        #         maxSum = max(crntSum,maxSum)
        # return maxSum
        
        maxSum = nums[0]
        crntSum = 0
        
        for num in nums:
            if crntSum<0:
                crntSum = 0
            crntSum+=num
            maxSum = max(crntSum,maxSum)
        
        return maxSum
            
                