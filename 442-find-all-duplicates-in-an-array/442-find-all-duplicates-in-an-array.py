class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
#         counter = collections.Counter(nums)
#         count = 0
#         for key,value in counter.items():
#             if value==2:
#                 nums[count] = key
#                 count+=1
        
#         while len(nums)>count:
#             nums.pop()
        
#         return nums

#         constant space O(1): but it doesnt include the output array
        ans = []
        for num in nums:
            if nums[abs(num)-1] <0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        
        return ans
            