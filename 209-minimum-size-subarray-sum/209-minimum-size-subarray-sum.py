class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2,3,1,2,4,3]  k = 7
        # |2|X |2,3|X |2,3,1|X  |2,3,1,2| yes -> decrease the window
        #  |3,1,2|X  |3,1,2,4|yes  |1,2,4|yes  |2,4|nope  |2,4,3| |4,3|
            
        
        total = 0
        count = len(nums)+1
        l,r = 0,0
        
        while l<=r and r<len(nums):
            total += nums[r]
            
            if total>=target:
                while l<=r and total>=target:
                    count = min(count,r-l+1)
                    if count==1:
                        return 1
                    total-=nums[l]
                    l+=1
            
            r+=1
        
        return 0 if count==len(nums)+1 else count
                