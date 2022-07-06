class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        n = len(counter)
        
        size = 0
        
        for key,val in counter.items():
            size += (val//2)*2
            counter[key] = val%2
            
            if counter[key] == 0:
                n-=1
        
        if size%2 == 0 and n>0:
            size += 1
        
        return size