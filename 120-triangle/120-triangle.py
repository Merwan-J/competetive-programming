class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = dict()
        
        def dfs(row,col):
            if row>=len(triangle) or col>=len(triangle[row]):
                return 0
            
            if (row,col) in dp:
                return dp[(row,col)]
                        
            dp[(row,col)] = triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))
            return dp[(row,col)]
        
        return dfs(0,0)