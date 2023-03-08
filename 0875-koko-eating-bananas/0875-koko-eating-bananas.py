class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def check(k):
            time = 0
            for pile in piles:
                time+=math.ceil(pile/k)
            
            return time
        
        
        l = 1
        r = max(piles)
        ans = r 
        
        while l<=r:
            mid = l + (r-l)//2
            
            if check(mid)<=h:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        
        return ans 
    