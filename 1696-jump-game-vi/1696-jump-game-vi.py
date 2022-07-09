class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [(-nums[0],0)]
        ans = nums[0]
        
        for i in range(1,n):
            while heap and heap[0][1]<i-k:
                heapq.heappop(heap)
            ans = nums[i] + -heap[0][0]
            heapq.heappush(heap,(-ans,i))
        
        return ans
        