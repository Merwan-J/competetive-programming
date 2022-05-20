class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = dict()
        row = dict()
        col = dict()
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]
                if cur=='.':
                    continue
#                 check for row
                if r in row:
                    if cur in row[r]:
                        return False
                    row[r] += cur
                else:
                    row[r] = [cur]
#                 check for col
                if c in col:
                    if cur in col[c]:
                        return False                
                    col[c] += cur
                else:
                    col[c] = [cur]
#                 chcek for squares
                sr,sc = r//3,c//3
                if (sr,sc) in square:
                    if cur in square[(sr,sc)]:
                        return False
                    square[(sr,sc)] += cur
                else:
                    square[(sr,sc)] = [cur]
#         check for the square
        
        
        return True
        