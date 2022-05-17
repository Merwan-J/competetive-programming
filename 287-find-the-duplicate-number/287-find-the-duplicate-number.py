class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#       Negative Marking - Lazy check constant Extra space O(1) but modifies the given array
        for num in nums:
            if nums[abs(num)-1]<0:
                return abs(num)
            nums[abs(num)-1] *=-1
          
#         Binary Search - without modifying the array and constand extra space O(1)

#         l,r  = 1,len(nums)-1
#         ans = -1
        
#         while l<=r:
#             mid = (l+r)//2
#             total = sum(num<=mid for num in nums)
            
#             if total > mid:
#                 ans = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
        
#         return ans
            
                
