class Solution:
    def rowCheck(self,board,row):
        numbers = [0]*10
        for c in range(9):
            num = board[row][c]
            if num and numbers[num] == 1:
                return False
            numbers[num] = 1
        return True
    
    def colCheck(self,board,col):
        numbers = [0]*10
        for r in range(9):
            num = board[r][col]
            if num and numbers[num] == 1:
                return False
            numbers[num] = 1
        
        return True
    
    def boxCheck(self,board,row,col):
        numbers = [0]*10
        for r in range(row,row+3):
            for c in range(col,col+3):
                num = board[r][c]
                if num and numbers[num] == 1:
                    return False
                numbers[num] = 1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col = 9,9
        
        for r in range(row):
            for c in range(col):
                if board[r][c].isalnum():
                    board[r][c] = int(board[r][c])
                else:
                    board[r][c] = 0
        
        for r in range(row):
            if self.rowCheck(board,r) is False:
                return False
        
        for c in range(col):
            if self.colCheck(board,c) is False:
                return False
        
        for r in range(0,row,3):
            for c in range(0,col,3):
                if self.boxCheck(board,r,c) is False:
                    return False
        
        return True
        