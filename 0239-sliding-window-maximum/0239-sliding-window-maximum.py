class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         what is the question asking:
#             to find the maximum in each window of size k in array nums
        
#         how can we do that?
#         monotonically decreasing stack???  - yea but we only want to know for k size window?
#         to do that we can remove elts that are not in our window from the front--- deque
        
#         monotonically decreasing queue
        
#         will keep a monotonically decreasing queue: that way what ever is at the front is the           max
        
#         when the front elt is not in the given window we remove it from the front
        
#         when the new elt that is going to be inserted is the max: we pop elts until it is not           there is no elts remaining or it is not max anymore
        
        
        ans = []
        dq = deque([])
        n = len(nums)
        l = 0
        
        for r in range(n):
            num = nums[r]
            
            # check for out of range elts in the front of the deque
            while dq and r-dq[0]+1>k:
                dq.popleft()
            
            # find the right place for num in the deque
            while dq and nums[dq[-1]]<num:
                dq.pop()
            
            dq.append(r)
            
            if r-l+1 == k:
                ans.append(nums[dq[0]])
                l+=1
        
        return ans
        
        
        
        