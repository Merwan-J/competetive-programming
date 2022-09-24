class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         @cache
#         def dfs(row,col):
#             if row == len(triangle):
#                 return 0
            
#             return triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))
        
#         return dfs(0,0)
            
        cur = [0]*(len(triangle)+1)
        prev = cur.copy()
        
        for row in range(len(cur)-2,-1,-1):
            for col in range(row,-1,-1):
                cur[col] = triangle[row][col] + min(prev[col],prev[col+1])
            prev = cur.copy()
        return cur[0]