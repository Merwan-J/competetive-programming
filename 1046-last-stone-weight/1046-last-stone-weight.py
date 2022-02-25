class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        
        heapq.heapify(arr)
        
        for i in stones:
            heapq.heappush(arr,-i)
        
        
        while True:
            if len(arr)<=1:
                return 0 if arr==[] else -arr[0]
            y = -1 * heapq.heappop(arr)
            x = -1 * heapq.heappop(arr)
            
            if y-x>0:
                heapq.heappush(arr,x-y)
        