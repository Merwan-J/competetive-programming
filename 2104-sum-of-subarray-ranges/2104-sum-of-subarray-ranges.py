class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            mmax = nums[i]
            mmin  = nums[i]
            for j in range(i+1,len(nums)):
                mmin = min(nums[j],mmin)
                mmax = max(nums[j],mmax)
                total += mmax-mmin
                
                
        
        return total