class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        """        
        def canEatAll(num,h):
            counter = 0
            for pile in piles:
                counter+=pile//num
                if pile%num!=0:
                    counter+=1
            return counter<=h
        
        k = max(piles)
        total = sum(piles)
        
        l,r = 1,k
        while l<=r:
            mid = l + (r-l)//2
            
            if canEatAll(mid,h):
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        
            
        return k    
            
                