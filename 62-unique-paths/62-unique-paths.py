class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        def dfs(row,col):
            if row==m-1 and col ==n-1:
                return 1
            
            if row>=m or col>=n:
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            memo[(row,col)] = dfs(row+1,col) + dfs(row,col+1)
            
            return memo[(row,col)]
            
            
        return dfs(0,0)
    
    