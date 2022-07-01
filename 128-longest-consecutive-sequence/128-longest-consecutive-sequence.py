class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
#         numsSet = set(nums)
#         ans = 0
        
#         for num in nums:            
#             i = 1
#             while num-i in numsSet:
#                 numsSet.remove(num-i)
#                 i+=1
            
#             j=1
#             while num+j in numsSet:
#                 numsSet.remove(num+j)
#                 j+=1
            
#             ans = max(ans,i+j-1)
            
#         return ans

        
        nums = set(nums)
        ans = 0
        
        for num in nums:
            if num-1 not in nums:
                i = 1
                while num+i in nums:
                    i+=1
                ans = max(ans,i)
        
        return ans
                
        
            
            