class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        psum = [0]
        
        for num in nums:
            psum.append(psum[-1]+num)
        
        
        """
        [1,3,4,2,5,0]
        
         0 1 2 3 4  5  6
        [0,1,4,8,10,15,15]
        
        
        15-1 = 14"""
        n = len(nums)
        stack = [-1]
        mod = 10**9 + 7
        ans = 0
        
        for i in range(n+1):
            while stack[-1] != -1 and (i == n or nums[i]<nums[stack[-1]]):
                ans = max(ans,nums[stack.pop()]*(psum[i]-psum[stack[-1] + 1]))
            stack.append(i)
        
        return ans%mod
                