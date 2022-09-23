class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
#         arr = sorted((num,i) for i,num in enumerate(nums))
#         stack = []
#         ans = 0
#         for tup in arr:
#             while stack and not(stack[-1][0]<=tup[0] and stack[-1][1]<=tup[1]):
#                 stack.pop()
#             stack.append(tup)
#             ans = max(ans,tup[1]-stack[0][1])
        
#         return ans

        rmax = nums.copy()
        for i in range(len(nums)-2,-1,-1):
            rmax[i]= max(rmax[i],rmax[i+1])
        
        l = 0
        ans = 0
        
        for r in range(len(nums)):
            while l<=r and  nums[l]>rmax[r]:
                l+=1
            ans = max(ans,r-l)
        
        return ans
                