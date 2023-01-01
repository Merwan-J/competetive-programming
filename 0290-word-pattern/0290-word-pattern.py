class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        # print(s,pattern)
        if len(s) != len(pattern):
            return False
        smap = {}
        pmap = {}
        
        for i in range(len(pattern)):
            a = pattern[i]
            b = s[i]
            
            if a in pmap and pmap[a] != b:
                return False
            if b in smap and smap[b] != a:
                return False
            
            if a not in pmap:
                pmap[a] = b
            
            if b not in smap:
                smap[b] = a
            
        return True
                