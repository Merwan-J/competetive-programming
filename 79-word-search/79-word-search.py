class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r<0 or c<0 or c == col or r == row or board[r][c]!=word[i] or board[r][c] == "#":
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            ans = False
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ans = ans or dfs(r+dr,c+dc,i+1)
            board[r][c] = temp
            
            return ans
        
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        
        return False
                    
                
                