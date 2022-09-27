class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for row in range(m):
                        if matrix[row][c]!=0:
                            matrix[row][c] = "x"
                    for col in range(n):
                        if matrix[r][col]!=0:
                            matrix[r][col] = "x"
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "x":
                    matrix[r][c] = 0
        
        