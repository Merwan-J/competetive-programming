class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [nums[0]]*len(nums)
        dpMin = [nums[0]]*len(nums)
        
        for i in range(1,len(nums)):
            cur = nums[i]
            dpMin[i] = min(dpMax[i-1]*cur,dpMin[i-1]*cur,cur)
            dpMax[i] = max(dpMax[i-1]*cur,dpMin[i-1]*cur,cur)
            
            # if cur>0:
            #     dpMax[i] = max(dpMax[i-1]*cur,cur)
            #     dpMin[i] = min(dpMin[i-1]*cur,cur)
            # else:
            #     dpMax[i] = max(dpMin[i-1]*cur,cur)
            #     dpMin[i] = min(dpMax[i-1]*cur,cur)
        
        return max(dpMax)