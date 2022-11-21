class Solution:
    def counter(self,s):
        ans = defaultdict(int)

        for char in s:
            ans[char] += 1

        return ans
    
    def contains(self,window,target):
        for key,val in target.items():
            if window[key]<val:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str: 
        n = len(s)
        target = self.counter(t)
        l = 0
        size = inf
        start,end = 0,0
        window = defaultdict(int)
        
        for r in range(n):
            window[s[r]]+=1
            while self.contains(window,target):
                if r-l+1<size:
                    size = r-l+1
                    start,end = l,r+1
                window[s[l]]-=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
        
        return s[start:end]
        
            
                
        
        
            