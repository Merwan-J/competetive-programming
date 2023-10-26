class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(counter,target):
            # print(counter,target)
            for key,val in target.items():
                if counter[key]<val:
                    # print('false')
                    return False
            # print("true")
            return True 
        
        
        n = len(s)
        window = defaultdict(int)
        target = Counter(t)
        ans = [0,0]
        found = False
        l = 0
        
        for r in range(n):
            window[s[r]] += 1
            
            while l<=r and check(window,target):
                if not found or ans[1]-ans[0]+1>r-l+1:
                    found = True
                    ans = [l,r]
                window[s[l]]-=1
                l+=1 
        
        return s[ans[0]:ans[1]+1] if found else ""