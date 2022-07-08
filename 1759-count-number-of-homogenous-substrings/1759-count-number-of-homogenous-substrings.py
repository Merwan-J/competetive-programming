class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1000000007
        ans = 0
        
        l = 0
        while l<len(s):
            r = l + 1
            while r<len(s) and s[r] == s[l]:
                r+=1
            n = r-l
            
            ans += n*(n+1)//2
            l = r
        
        return ans%mod
        