class Solution:
    def halvesAreAlike(self, s: str) -> bool:        
        l = 0
        r = len(s)- 1
        
        left_count = 0
        right_count = 0
        
        while l<r:
            if s[l] in  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                left_count+=1
            if s[r] in  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                right_count+=1
            
            l+=1
            r-=1
        return left_count == right_count