class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def calculate(num):
            total = 0
            for i in time:
                total+= num//i
            
            return total
        
        l,r = 1,min(time)*totalTrips
        
        while l<=r:
            mid = (l+r)//2
            midTime = calculate(mid)
            
            if midTime<totalTrips:
                l = mid + 1
            else:
                r = mid - 1
            
        return l
                
            