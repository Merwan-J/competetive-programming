class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         top down approach

#         dp = {}
    
#         def dfs(row,col):
#             if row==len(matrix)-1 and col<len(matrix[0]) and col>-1:
#                 return matrix[row][col]
            
#             if row>=len(matrix) or col>=len(matrix[0]) or col<0:
#                 return float('inf')
            
#             if (row,col) in dp:
#                 return dp[(row,col)]
            
#             dp[(row,col)] = matrix[row][col] + min(dfs(row + 1, col - 1), dfs(row + 1, col),dfs(row + 1, col + 1))
            
#             return dp[(row,col)]
        
#         ans = float('inf')
        
#         for c in range(len(matrix[0])):
#             ans = min(ans,dfs(0,c))
#         return ans



#           Bottom up approach - O(1) auxiliary space - in place
        
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row-2,-1,-1):
            for c in range(col-1,-1,-1):
                left = matrix[r+1][c-1] if c-1>-1 else float('inf')
                right = matrix[r+1][c+1] if c+1<row else float('inf')
                below = matrix[r+1][c]
                
                matrix[r][c] += min(left,right,below)
        return min(matrix[0])
                


                