class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i,target,count):
            if count == 0:
                return target == 0
            
            if i == n:
                return False
            
            ans = False
            
            if target>=nums[i]:
                ans = ans or dfs(i+1,target-nums[i],count-1)
            ans = ans or dfs(i+1,target,count)
            
            return ans
        
        
        for size in range(1,n):
            if (total*size)%n == 0 and dfs(0,(total*size)//n,size):
                return True
        return False