class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        total = 0
        
        for num in nums:
            total+=num
            heapq.heappush(heap,-num)
        
        target = total/2
        count = 0
        
        while total>target:
            curNum = -heappop(heap) 
            total-=curNum/2
            heappush(heap,-(curNum-curNum/2))
            count += 1
            
        return count