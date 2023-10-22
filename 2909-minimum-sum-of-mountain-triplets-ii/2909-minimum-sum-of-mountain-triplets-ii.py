class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        leftMin = [inf]*n
        rightMin = [inf]*n
        
        for i in range(1,n):
            leftMin[i] = min(leftMin[i-1],nums[i-1])
        
        for i in range(n-2,-1,-1):
            rightMin[i] = min(rightMin[i+1],nums[i+1])
        
        ans = inf
        for i in range(1,n-1):
            curNum = nums[i]
            
            if curNum>leftMin[i] and curNum>rightMin[i]:
                ans = min(ans,curNum+leftMin[i]+rightMin[i])
        
        return -1 if ans == inf else ans 
            