class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary = 0
        secondary = n-1
        total = 0
        
        
        for row in range(n):
            total+=mat[row][primary] + mat[row][secondary]
            
            if primary == secondary:
                total-=mat[row][secondary]
            
            primary+=1
            secondary-=1
        
        return total
        
        