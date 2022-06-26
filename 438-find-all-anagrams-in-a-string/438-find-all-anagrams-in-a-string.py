class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = collections.Counter(p)
        run = collections.Counter(s[:len(p)])
        ans = []
        
        if run == counter:
            ans.append(0)
        
        l,r = 0,len(p)
        
        while r<len(s):
            run[s[r]] = run.get(s[r],0)+1
            run[s[l]] -= 1
            
            if run == counter:
                ans.append(l+1)
            
            l+=1
            r+=1
        
        return ans