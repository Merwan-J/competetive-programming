class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0]*26
        ans = 1
        
        l,r = 0,0
        while l<=r and r<len(s):
            n = r-l+1
            char[ord(s[r])-ord('A')] += 1
            moves = n-max(char)
            
            if moves<=k:
                ans = max(ans,n)
            else:
                while moves>k:
                    char[ord(s[l])-ord('A')]-=1
                    n-=1
                    moves = n-max(char)
                    l+=1
            r+=1
        
        return ans