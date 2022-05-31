class Solution:
    def climbStairs(self, n: int) -> int:
#         bottom up
        memo = {1:1,2:2}
        
#         for i in range(3,n+1):
#             memo[i] = memo[i-1] + memo[i-2]
        
#         return memo[n]


#     top down
        def helper(n):
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)