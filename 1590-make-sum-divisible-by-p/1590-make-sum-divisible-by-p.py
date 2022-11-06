class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #get the sum of the array
        total = sum(nums)
        # to check for divisiblity by p
        if total%p == 0:
            return 0
        # if p>total:
        #     return -1
        # initialize vars : psum,ans,lookup
        psum = 0
        ans = inf
        lookup = {0:-1}
        # find for possible subarray
        for i,num in enumerate(nums):
            psum+=num
            target = (psum-total)%p
            if target in lookup:
                ans = min(ans,i-lookup[target])
            lookup[psum%p] = i
        # check if the subarray is found else return -1 
        
        return -1 if ans == inf or ans == len(nums) else ans