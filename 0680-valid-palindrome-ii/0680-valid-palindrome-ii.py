class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        
        while l<=r:
            if s[l] != s[r]:
                skipR = s[l:r]
                skipL = s[l+1:r+1]
                
                return skipR == skipR[::-1] or skipL == skipL[::-1]
            
            l+=1
            r-=1
        
        return True
        