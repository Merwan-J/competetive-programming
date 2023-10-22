class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [0]*n
        
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],nums[i+1])
            
        ans = 0
        curMax = nums[0]
        for i,num in enumerate(nums):
            ans = max(ans,rightMax[i]*(curMax-num))
            curMax = max(curMax,num)
            
        return ans 