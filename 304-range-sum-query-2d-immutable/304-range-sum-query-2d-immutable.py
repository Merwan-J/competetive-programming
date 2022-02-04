class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for j in range(len(self.matrix)):
            prefix = [0]
            for i in self.matrix[j]:
                prefix.append(prefix[-1]+i)
            self.matrix[j] = prefix
            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1,row2+1):
            sum+=self.matrix[i][col2+1]-self.matrix[i][col1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)