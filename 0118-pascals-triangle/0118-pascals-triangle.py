class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        
        if n<3:
            return ans[:n]
        
        for row in range(2,n):
            temp = [1]
            
            for col in range(1,row):
                temp.append(ans[-1][col]+ans[-1][col-1])
                
            temp.append(1)
            ans.append(temp)
        
        return ans