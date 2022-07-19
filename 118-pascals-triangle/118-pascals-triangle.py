class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        ans = [[1]]
        if rows == 1:
            return ans
        ans.append([1,1])
        
        for i in range(2,rows):
            temp = [1]
            
            for i in range(len(ans[-1])-1):
                temp.append(ans[-1][i]+ans[-1][i+1])
            
            temp.append(1)
            ans.append(temp)
        return ans