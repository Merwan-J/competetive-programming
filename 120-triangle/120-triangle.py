class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dfs(row,col):
            if row == len(triangle):
                return 0
            
            return triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))
        
        return dfs(0,0)
            
            