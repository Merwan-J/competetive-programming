class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        run = collections.Counter(s2[:len(s1)])
        
        if run==counter:
            return True
        # print(run)
        
        l,r = 0,len(s1)
        while r<len(s2):
            run[s2[r]] = run.get(s2[r],0) + 1
            run[s2[l]] -= 1
            
            if run[s2[l]] == 0:
                del run[s2[l]]
            if run == counter:
                return True
            
            r+=1
            l+=1
        
        return False
            