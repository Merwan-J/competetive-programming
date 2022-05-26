class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,r = max(weights), sum(weights)
        
        while l<=r:
            mid = (l+r)//2
            total = 0
            count = 1
            for w in weights:
                if total + w > mid:
                    count += 1
                    total = 0
                total += w
                
            if count>days:
                l = mid + 1
            else:
                r = mid - 1
                
        return l            
            