class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = []
        def isValid(row,col):
            return row>=0 and col>= 0 and row<len(board) and col<len(board[0])
        
        def dfs(row,col):
            if not isValid(row,col) or board[row][col] != 'O':
                return
            board[row][col] = 'M'
            
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (row in [0,len(board)-1] or col in [0,len(board[-1])-1]):
                    dfs(row,col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'M':
                    board[row][col] = "O"
                elif board[row][col] == 'O':
                    board[row][col] = "X"
        