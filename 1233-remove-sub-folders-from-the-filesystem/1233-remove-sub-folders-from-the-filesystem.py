class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))    
        ans = set()
        
        for f in folder:
            for i in range(1, len(f)):
                if f[i] == '/' and f[: i] in ans:
                    break
                if i==len(f)-1:
                    ans.add(f)
        
        return list(ans)
    
        