class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []
        path = []
        
        def dfs(i):
            if i == len(s):
                ans.append("".join(path))
                return
            
            char = s[i]
            path.append(char)
            dfs(i+1)
            path.pop()
            
            if char.isalpha():
                char = char.upper() if char.islower() else char.lower()
                path.append(char)
                dfs(i+1)
                path.pop()
            
            
        
        dfs(0)
        return ans
            