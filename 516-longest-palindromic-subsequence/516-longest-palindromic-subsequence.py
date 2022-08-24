class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
#         @cache
#         def dp(l,r):
#             if l>r:
#                 return 0
            
#             ans = 0
#             if s[l]==s[r]:
#                 ans = dp(l+1,r-1)
#                 ans = ans + 1 if l==r else ans + 2
#             else:
#                 ans = max(ans,dp(l+1,r),dp(l,r-1))
#             return ans
        
#         return dp(0,len(s)-1)


        r = s[::-1]
        @cache
        def dp(i,j):
            if i>=len(s) or j>=len(r):
                return 0
            
            ans = 0
            if s[i] == r[j]:
                ans = max(ans,1+dp(i+1,j+1))
            else:
                ans = max(dp(i+1,j),dp(i,j+1),ans)
            
            return ans
        
        return dp(0,0)