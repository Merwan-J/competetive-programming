class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter  = collections.Counter(s)
        
        
        prev = -1
        for char,count in counter.items():
            if prev!=count and prev!=-1:
                return False
            prev = count
        
        return True