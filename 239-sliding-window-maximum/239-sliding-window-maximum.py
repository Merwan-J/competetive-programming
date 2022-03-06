class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        deleted = dict()
        
        for i in range(k):
            heapq.heappush(heap,-nums[i])
            deleted[nums[i]] = deleted.get(nums[i],0)+1
        
        l,r = 1, k
        ans = [-heap[0]]
        while r<len(nums):
            deleted[nums[l-1]] -= 1
            deleted[nums[r]] = deleted.get(nums[r],0)+1
            heapq.heappush(heap,-nums[r])
            
            while deleted[-heap[0]]==0:
                heapq.heappop(heap)
            ans.append(-heap[0])
            l+=1
            r+=1
        
        return ans