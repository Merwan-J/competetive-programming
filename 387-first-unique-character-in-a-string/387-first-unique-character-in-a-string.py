class Solution:
    def firstUniqChar(self, s: str) -> int:
        
                
            
        counter = dict()
        
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] = (i,counter[s[i]][1]+1)
            else:
                counter[s[i]] = (i,0)
        
        for char, tup in counter.items():
            if tup[1] == 0:
                return tup[0]
        
        return -1