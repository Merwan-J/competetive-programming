class Solution:
    def isInterleave(self, s: str, t: str, p: str) -> bool:
        if len(s)+len(t)<len(p):
            return False
        if len(s)+len(t)>len(p):
            return False
        
        @cache
        def dp(i_p,i_s,i_t):
            if i_p>=len(p):
                return True
            
            if i_s>=len(s) and i_t>=len(t):
                return True
            
            ans = False
            
            if i_s<len(s) and p[i_p] == s[i_s]:
                ans = dp(i_p+1,i_s+1,i_t)
            if i_t<len(t) and p[i_p] == t[i_t]:
                ans = ans or dp(i_p+1,i_s,i_t+1)
            
            return ans
        
        return dp(0,0,0)