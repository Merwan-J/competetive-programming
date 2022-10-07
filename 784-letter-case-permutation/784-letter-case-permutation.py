class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        path = []
        ans = []
        
        def dfs(i):
            if i == len(s):
                ans.append("".join(path))
                return
            
            path.append(s[i])
            dfs(i+1)
            path.pop()
            if s[i].isalpha(): 
                if s[i] == s[i].lower():
                    path.append(s[i].upper())
                else:
                    path.append(s[i].lower())
                dfs(i+1)
                path.pop()
        
        dfs(0)
        
        return ans
            