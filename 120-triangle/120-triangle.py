class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#         top down
#         dp = dict()
        
#         def dfs(row,col):
#             if row>=len(triangle) or col>=len(triangle[row]):
#                 return 0
            
#             if (row,col) in dp:
#                 return dp[(row,col)]
                        
#             dp[(row,col)] = triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))
#             return dp[(row,col)]
        
#         return dfs(0,0)
    
#         bottom up with O(n) space complexity

        dp = [0]*(len(triangle)+1)
        
        for r in range(len(triangle)-1,-1,-1):
            row = triangle[r]
            for i,val in enumerate(row):
                dp[i] = val + min(dp[i],dp[i+1])
        return dp[0]