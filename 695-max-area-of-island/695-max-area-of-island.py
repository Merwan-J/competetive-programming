class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = []
        area = 0
        def isValid(row,col):
            return row>=0 and row<len(grid) and col>=0 and col<len(grid[0])
        
        def dfs(row,col,count):
            if (row,col) in visited or not isValid(row,col) or grid[row][col]==0:
                return count
            
            visited.append((row,col))

            up = dfs(row+1,col,0)
            down = dfs(row-1,col,0)
            right = dfs(row,col+1,0)
            left = dfs(row,col-1,0)
            
            return up + down + right + left + 1
            
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area = max(area,dfs(row,col,0))
        
        return area
                    