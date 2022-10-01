class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @cache
        def dp(l,r):
            if l+r ==len(s3):
                return True
            
            ans = False
            if l<len(s1) and s1[l] == s3[l+r]:
                ans = ans or dp(l+1,r)
            if r<len(s2) and s2[r]==s3[l+r]:
                ans = ans or dp(l,r+1)

            return ans

        return dp(0,0)