class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        stack = []
        
        for i in range(n):
            start,end = points[i]
            while stack and start<=stack[-1][1]:
                end = min(end,stack.pop()[1])
            stack.append([start,end])
        
        return len(stack)
        
        