class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        isValid = lambda r,c: r<m and c<n and r>-1 and c>-1
        #(row - 1, col + 1), (row, col + 1) and (row + 1, col + 1)

        for c in range(n-1,-1,-1):
            for r in range(m):
                for dr,dc in [(-1,1),(0,1),(1,1)]:
                    nr,nc = r+dr,c+dc

                    if isValid(nr,nc) and grid[nr][nc]>grid[r][c]:
                        dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])

        #take the max out of the first column dp grid 
        ans = 0

        for r in range(m):
            ans = max(ans,dp[r][0])

        return ans 