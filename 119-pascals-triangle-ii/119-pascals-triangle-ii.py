class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1],[1,1]]
        
        if rowIndex<2:
            return ans[rowIndex]
        
        for row in range(2,34):
            temp = [1]
            
            for col in range(1,row):
                temp.append(ans[-1][col]+ans[-1][col-1])
                
            temp.append(1)
            if rowIndex == row:
                return temp
            ans.append(temp)
        
        