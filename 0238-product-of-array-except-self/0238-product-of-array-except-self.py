class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [1]*n
        
        
        for i in range(1,n):
            ans[i] = nums[i-1]*ans[i-1]
        
        right = nums[n-1]
        for i in range(n-2,-1,-1):
            ans[i] *= right
            right *= nums[i]
        
        return ans 
        
            