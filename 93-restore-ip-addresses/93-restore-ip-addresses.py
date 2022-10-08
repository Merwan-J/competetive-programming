class Solution:
    def restoreIpAddresses(self, ip: str) -> List[str]:
        ans = []
        path = []

        def dfs(i):
            if len(path) == 4:
                if i<len(ip):
                    return
                ans.append(".".join(path))
                return
            if i >= len(ip):
                return
            
            
            for j in range(i,i+3):
                if j == len(ip):
                    break
                
                s = ip[i:j+1]
                if s[0] == "0" and len(s)>1:
                    continue
                if int(s)<256:
                    path.append(s)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        
        return ans