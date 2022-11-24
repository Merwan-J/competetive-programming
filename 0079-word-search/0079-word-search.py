class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        self.found = False
        
        def dfs(r,c,i):
            if i == len(word):
                self.found = True
                return True
            
            if self.found:
                return True
            
            temp = board[r][c]
            board[r][c] = "#"
            
            ans = False
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if -1<nr<row and -1<nc<col and board[nr][nc] == word[i]:   
                    ans = ans or dfs(nr,nc,i+1)
            board[r][c] = temp
            return ans
        
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r,c,1):
                    return True
        
        return False
                    
                
                