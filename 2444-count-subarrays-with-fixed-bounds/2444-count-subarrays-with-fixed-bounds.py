class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastInvalid = -1
        maxPos = -1
        minPos = -1
        ans = 0
        
        for i,num in enumerate(nums):
            if not minK<=num<=maxK:
                lastInvalid = i
            
            if num == maxK:
                maxPos = i
            if num == minK:
                minPos = i
            
            ans += max(0, min(maxPos,minPos) - lastInvalid )
        
        return ans 