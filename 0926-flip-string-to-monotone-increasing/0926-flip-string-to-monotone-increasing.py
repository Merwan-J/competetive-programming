class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total = [0,0]
        sofar = [0,0]
        ans = inf
        
        for char in s:
            total[int(char)]+=1
        
        for char in s:
            ans = min(ans,sofar[1] + total[0]-sofar[0])
            sofar[int(char)]+=1
        
        return min(ans,total[1])