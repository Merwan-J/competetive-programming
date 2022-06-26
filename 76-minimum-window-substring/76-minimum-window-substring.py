class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        run = {}
        need,have = len(counter),len(run)
        
        start,end = 0,0
        minLen = float('inf')
        
        l = 0
        for i in range(len(s)):
            run[s[i]] = run.get(s[i],0) + 1
            
            if s[i] in counter and run[s[i]] == counter[s[i]]:
                have += 1
            
            while have == need:
                if i-l+1 < minLen:
                    minLen = i-l+1
                    start,end = l,i
                
                run[s[l]] -= 1
                if s[l] in counter and run[s[l]]<counter[s[l]]:
                    have -= 1
            
                l += 1
        
        return "" if minLen == float('inf') else s[start:end+1]
                
                
        
        
        
        
        
                
        