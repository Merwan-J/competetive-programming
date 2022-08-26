class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        l,r,count = 0,0,0
        
        while l<len(g) and r<len(s):
            if g[l] <=s[r]:
                r+=1
                count+=1
            l+=1

        
        return count
        