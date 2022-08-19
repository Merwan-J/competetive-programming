class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isPossible(limit):
            i = 0
            count = 0
            while i<len(weights):
                total = 0
                while i<len(weights):
                    if total + weights[i]<=limit:
                        total += weights[i]
                        i+=1
                    else:
                        break
                count += 1
            
            return count
        
        
        
        l,r = max(weights), sum(weights)
        
        while l<=r:
            mid = (l+r)//2
            day = isPossible(mid)
        
            if day>days:
                l = mid + 1
            else:
                r = mid - 1
        return l            
            