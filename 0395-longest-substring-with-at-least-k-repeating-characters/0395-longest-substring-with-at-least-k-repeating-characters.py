class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def check(counter,k):
            if len(counter)==0:
                return False
            
            for char,count in counter.items():
                if count<k:
                    return False
            
            return True 
        
        n = len(s)
        counter = Counter(s)
        uniqueChars = len(counter)
        ans = 0
        
        for size in range(1,uniqueChars+1):
            l = 0
            curFreq = {}
            
            for r in range(n):
                curFreq[s[r]] = curFreq.get(s[r],0)+1
                
                while len(curFreq)>size:
                    curFreq[s[l]]-=1
                    if curFreq[s[l]] == 0:
                        del curFreq[s[l]]
                    l+=1
                
                if check(curFreq,k):
                    ans = max(ans,r-l+1)
        
        return ans 
        
        
        
            