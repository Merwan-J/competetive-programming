class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # if len(nums)==1:
        #     return 1
        count = 0
        zeros = 0
        l,r = 0,0
        
        
        [1,1,1,0,0,0,1,1,1,1,0]
        # |1,1| |1,1,1|  |1,1,1,0|zero |1,1,1,0,0| count |1,1,1,0,0,0| zero exceeds 
        
        while l<=r and r<len(nums):
            if nums[r]==0:
                zeros+=1
                if zeros<=k:
                    count = max(count,r-l+1)
                while zeros>k:
                    if nums[l]==0:
                        zeros-=1
                    l+=1
            count = max(count,r-l+1)
            r+=1
        
        return count
                
                
            