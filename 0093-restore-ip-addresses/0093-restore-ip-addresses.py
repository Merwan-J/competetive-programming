class Solution:
    def restoreIpAddresses(self, ip: str) -> List[str]:
        
        
#         two conditions: no leading zero and the number has to be between 0 and 255 
#         and it has to be 4 divisions: how to figure it out ???
            
        
        path = []
        ans = []
        
        def dfs(i):
            if i == len(ip) and len(path) == 4:
                ans.append(".".join(path))
                return
            
            if len(path)>3 or i>=len(ip):
                return
            
            for j in range(1,4):
                if int(ip[i:i+j])<256:
                    if j>1 and ip[i] == "0":
                        break
                    path.append(ip[i:i+j])
                    dfs(i+j)
                    path.pop()
            
        dfs(0)
        return ans
                
            
        
        
        
        
        
        