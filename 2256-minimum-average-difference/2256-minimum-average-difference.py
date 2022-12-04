class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        minDiff = float("inf")
        ans = 0
        total = sum(nums)
        runSum = 0
        n = len(nums)
        
        for i in range(n):
            runSum+=nums[i]
            
            left = runSum//(i+1)
            right = 0 
            if i<n-1:
                right = (total-runSum)//(n-i-1)
                
            if abs(right-left)<minDiff:
                minDiff = abs(right-left)
                ans = i
        
        return ans
        
        