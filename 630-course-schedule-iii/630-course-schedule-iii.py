class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda item: item[1])
        heap = []
        time = 0
        
        for i in range(len(courses)):
            dur,last = courses[i]
            
            time += dur
            heapq.heappush(heap,-dur)
            
            if time>last:
                time+=heapq.heappop(heap)
    
        return len(heap)