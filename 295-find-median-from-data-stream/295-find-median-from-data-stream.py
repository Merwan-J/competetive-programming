class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        
        if self.large and self.small and self.large[0] < -self.small[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        if len(self.large) > len(self.small)+1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small,val)
        if len(self.small) > len(self.large)+ 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)

    def findMedian(self) -> float:
        if len(self.large)> len(self.small):
            return self.large[0]
        if len(self.small)>len(self.large):
            return -self.small[0]
        
        return (self.large[0]-self.small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()