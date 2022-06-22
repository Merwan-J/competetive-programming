class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        toMin = lambda time: int(time[0])*60 + int(time[1])
        
        for i in range(len(timePoints)):
            timePoints[i] = toMin(timePoints[i].split(":"))
        
        timePoints.sort()
        
        ans = float('inf')
        for i in range(len(timePoints)-1):
            cur = timePoints[i]
            next = timePoints[i+1]

            ans = min(ans,next-cur)
            
        
        return min(ans,24*60-timePoints[-1] + timePoints[0])