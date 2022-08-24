class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(l,r):
            if l>r:
                return 0
            
            ans = 0
            if s[l]==s[r]:
                ans = dp(l+1,r-1)
                ans = ans + 1 if l==r else ans + 2
            else:
                ans = max(ans,dp(l+1,r),dp(l,r-1))
            return ans
        
        return dp(0,len(s)-1)