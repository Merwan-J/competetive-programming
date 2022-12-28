class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        total = 0
        
        
        for stones in piles:
            total+=stones
            heapq.heappush(heap,-stones)
        
        while k:
            curStones = -heappop(heap) 
            total-=curStones//2
            heappush(heap,-(curStones-curStones//2))
            k-=1
            
        return total