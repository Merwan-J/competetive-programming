class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = collections.defaultdict(int)
        ans = 0
        
        for t in time:
            t_mod = t%60
            
            find = 0 if t_mod == 0 else 60 - t_mod
            ans += count[find]
            count[t_mod]+=1 
        
        return ans