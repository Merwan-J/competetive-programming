class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod =  10 ** 9 + 7
        nums.sort()
        
        l,r = 0,len(nums)-1
        count = 0
        
        while l<=r:
            total = nums[l] + nums[r]
            
            if total<=target:
                count+=pow(2, r - l, mod) 
                l+=1
            else:
                r-=1
        
        return count%mod
        