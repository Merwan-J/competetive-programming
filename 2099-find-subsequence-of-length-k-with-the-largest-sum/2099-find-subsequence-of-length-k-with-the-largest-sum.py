class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums = [(nums[i],i) for i in range(len(nums))]
        heapq.heapify(nums)


        while len(nums)>k:
            heapq.heappop(nums)

        ans = sorted(nums,key=lambda item: item[1])
        
        return [item[0] for item in ans]
        