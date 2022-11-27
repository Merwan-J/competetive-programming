class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        
        for brace in s:
            if brace == ")" and opened>0:
                opened-=1
            elif brace == ")":
                closed+=1
            else:
                opened+=1
        
        return opened+closed