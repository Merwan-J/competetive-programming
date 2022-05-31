class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0,1:0}
        n = len(cost)
        def helper(n):
            if n in memo:
                return memo[n]
            
            memo[n] = min(helper(n-1)+cost[n-1],helper(n-2)+cost[n-2])
            
            return memo[n]
        
        return helper(n)