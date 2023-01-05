class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item: item[1])
        
        i = 0
        arrows = 0
        
        while i<len(points):
            cur = points[i]
            arrows += 1
            i += 1
            
            while i<len(points):
                friend = points[i]
                if friend[0] > cur[1]:
                    break
                i+=1
        
        return arrows
                    
            