class Solution:
    def tribonacci(self, n: int) -> int:
#         top down
        memo = {0:0,1:1,2:1}
        
        def helper(i):
            if i in memo:
                return memo[i]
            
            if i<0:
                return 0
            
            memo[i] = helper(i-1) + helper(i-2) + helper(i-3)
            
            return memo[i]
            
        return helper(n)
    
    
#     bottom up
        memo = [0,1,1] + [0]*(n-2)
        
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
        return memo[n]