class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        
        nums.sort()
        maxx = nums[-1]
        minn = nums[0]
        diff = maxx-minn
        
        for i in range(len(nums)-1):
            cur_min = min(minn+k,nums[i+1]-k)
            cur_max = max(maxx-k,nums[i]+k)
            diff = min(cur_max-cur_min,diff)
        
        return diff
        