class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         [1,2,3,4]
#   prefix[1,1,2,6]
#   suffix[24,12,4,1]
#      arr[24,12,8,6]

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        arr = []
        
#       prefix
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1] 
        
#       suffix
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        
        for i in range(len(nums)):
            arr.append((prefix[i]*suffix[i]))
        
        return arr