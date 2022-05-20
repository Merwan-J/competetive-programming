class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        

        self.sub = True
        
        def dfs(row,col):
            if row>=0 and col>=0 and row<len(grid2) and col<len(grid2[0]) and grid2[row][col] == 1:
                grid2[row][col] = 0
                if grid1[row][col] == 0:
                    self.sub = False
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
                
                
        count = 0
        
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    self.sub = True
                    dfs(r,c)
                    if self.sub == True:
                        count += 1
        
        return count
        
       
        
        