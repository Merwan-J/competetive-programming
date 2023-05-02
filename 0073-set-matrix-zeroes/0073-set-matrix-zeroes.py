class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for r in zeroRows: 
            for c in range(cols):
                matrix[r][c] = 0
        
        for c in zeroCols:
            for r in range(rows):
                matrix[r][c] = 0 
            