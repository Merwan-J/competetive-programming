class Solution:
    def isInterleave(self, s: str, t: str, p: str) -> bool:
        if len(s)+len(t) != len(p):
            return False 
        
        @cache
        def dp(m,n):
            if m+n>=len(p):
                return True
            
            if m>=len(s) and n>=len(t):
                return True
            
            ans = False
            if m<len(s) and p[m+n] == s[m]:
                ans = dp(m+1,n)
            if n<len(t) and p[m+n] == t[n]:
                ans = ans or dp(m,n+1)
            
            return ans
        
        return dp(0,0)