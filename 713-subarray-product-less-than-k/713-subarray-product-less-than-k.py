class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(i,len(nums)):
        #         total*=nums[j]
        #         if total>=k:
        #             break
        #         count+=1
        # return count
        
#     [10,5,2,6], k = 100
#  [10]  [10,5] [10,5,2] [5,2] [5,2,6] 
# [10] count [10,5] count [5] count [10,5,2] stop [5,2] count [2] count []

        if k<=1:
            return 0
        
        total = 1
        count = 0
        l,r = 0,0
        
        while r<len(nums):
            total = total*nums[r]
            while total>=k:
                total/=nums[l]
                l+=1
            count += r-l+1
            r+=1
        return count
            
    
    