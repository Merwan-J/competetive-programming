class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        valid = lambda row,col: row>-1 and row<m and col>-1 and col<n
        
        memo = {}
        def dfs(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            num = matrix[row][col]
            
            up = dfs(row-1,col) if valid(row-1,col) and num<matrix[row-1][col] else 0    
            down = dfs(row+1,col) if valid(row+1,col) and num<matrix[row+1][col] else 0   
            left =dfs(row,col-1) if valid(row,col-1) and num<matrix[row][col-1] else 0   
            right = dfs(row,col+1) if valid(row,col+1) and num<matrix[row][col+1] else 0    
            memo[(row,col)] = 1 + max(up,left,right,down)
            return memo[(row,col)]
        ans = 0
        
        for row in range(m):
            for col in range(n):
                ans = max(ans,dfs(row,col))
        
        return ans