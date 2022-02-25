class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0])
            
        heapq.heapify(matrix)
        
        for i in matrix:
            heapq.heapify(i)
        
        ans = []
        heapq.heapify(ans)
        
        while len(ans)<k:
            x = heapq.heappop(matrix)

            heapq.heappush(ans,heapq.heappop(x))
            if x!=[]:
                heapq.heappush(matrix,x)

        for i in range(k):
            if i==k-1:
                return heapq.heappop(ans)
            heapq.heappop(ans)
        