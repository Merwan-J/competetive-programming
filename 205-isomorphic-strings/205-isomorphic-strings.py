class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tmap = {}
        smap = {}
        
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if b in tmap and tmap[b] != a:
                return False
            if a in smap and smap[a] != b:
                return False
            
            if a not in smap:
                smap[a] = b
            if b not in tmap:
                tmap[b] = a
        return True
                
                
            