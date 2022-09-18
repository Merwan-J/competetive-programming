class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
#         @cache
#         def dfs(i):
#             if i>=len(questions):
#                 return 0
#             solve = questions[i][0] + dfs(i+1+questions[i][1])
#             skip = dfs(i+1)
            
#             return max(solve,skip)
        
#         return dfs(0)
        m = len(questions)
        dp = [0]*(m+1)
        
        for i in range(m-1,-1,-1):
            solve,skip = questions[i][0],dp[i+1]
            next = i + questions[i][1]+1
            if next<m:
                solve += dp[next]
            dp[i] = max(solve,skip)
        
        return dp[0]