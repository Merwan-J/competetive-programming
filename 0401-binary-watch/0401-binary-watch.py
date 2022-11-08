class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = set()
        
        def dfs(i,j,count,h,m):
            if count == 0:
                ans.add(str(h)+":"+"0"*(m<10)+str(m))
                return
            
            if i >= 4 and j>=6:
                return
            dfs(i+1,j+1,count,h,m)
            if i<4 and h+2**i < 12:
                dfs(i+1,j,count-1,h+2**i,m)
                
            if j<6 and m+2**j < 60:
                dfs(i,j+1,count-1,h,m+2**j)
        
        dfs(0,0,turnedOn,0,0)
        return list(ans)
