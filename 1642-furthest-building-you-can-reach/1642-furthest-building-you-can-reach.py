class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(h)):
            d = 0 if i==len(h)-1 else h[i+1] - h[i]
            if d>0:
                if b>=d:
                    b-=d
                    heapq.heappush(heap,-d)
                elif l>0:
                    if heap and -heap[0] > d:
                        b+= -heap[0]
                        b-=d
                        heapq.heappop(heap)
                        heapq.heappush(heap,-d)
                    l-=1
                else: 
                    break
        
        return i
        