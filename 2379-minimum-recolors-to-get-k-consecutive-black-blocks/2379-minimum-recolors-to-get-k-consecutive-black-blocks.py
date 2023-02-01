class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        n = len(blocks)
        l = 0
        white = 0
        ans = inf
        
        for r in range(n):
            if blocks[r] == "W":
                white+=1
                
            if r-l+1 == k: 
                ans = min(ans,white)
                white -= blocks[l] == "W"
                l+=1
        
        return ans
            