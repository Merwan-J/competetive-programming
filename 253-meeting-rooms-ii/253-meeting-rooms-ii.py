class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda item: item[0])
        heap = [intervals[0][1]]
        rooms = 1
        
        for i in range(1,len(intervals)):
            cur = intervals[i]
            if cur[0]<heap[0]:
                rooms += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap,cur[1])
        
        return rooms