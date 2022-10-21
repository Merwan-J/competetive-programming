class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         self.found = False
        
#         @lru_cache(None)
#         def dp(i,cur):
#             nonlocal total
#             if total-cur == cur or self.found:
#                 self.found = True
#                 return True
#             if i == len(nums) or total-cur<cur:
#                 return False
            
#             return dp(i+1,cur+nums[i]) or dp(i+1,cur)
        
#         return dp(0,0)
        target = sum(nums)//2
        if target!=sum(nums)-target:
            return False
        
        n = len(nums)
        dp = [[False]*(target+1) for r in range(n)]
        dp[0][0] = True
        
        for i in range(n-1):
            for j in range(target+1):
                if dp[i][j]:
                    dp[i+1][j] = True
                    if j+nums[i]<=target:
                        dp[i+1][j+nums[i]] = True
        
        return sum([dp[i][target] for i in range(n) if dp[i][target] == True]) > 0
                    
                    