class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        b_count = res = 0
        
        for c in s:
            if c == 'a':
                res = min(res+1, b_count)
            else:
                b_count += 1
                
        return res