class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(target):
            ans = 0
            for num in time:
                ans+=target//num
            
            return ans
        
        
        l = 1
        r = min(time)*totalTrips
        ans = -1
        

        while l<=r:
            mid = l + (r-l)//2
            if check(mid)>=totalTrips:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans 
        
        
        