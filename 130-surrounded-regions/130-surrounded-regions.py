class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col = len(board),len(board[0])
        
        visited = set()
        
        def dfs(r,c):
            if r<0 or c<0 or r == row or col == c or board[r][c] == "X" or (r,c) in visited:
                return
            board[r][c] = ""
            visited.add((r,c))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: dfs(r+dr,c+dc)
                
        
        for r in range(row):
            for c in range(col):
                if (r == 0 or r == row-1 or c == 0 or c == col-1) and board[r][c] == "O":
                    dfs(r,c)
        
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] ="X"