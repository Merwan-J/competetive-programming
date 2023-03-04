class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        
#         subarray ending at pos
        
#         total subarray given length n 


        psum = 0
        count = 0
        left = 0
        n = len(nums)
        
        for right in range(n):
            psum+=nums[right]
            
            while psum*(right-left+1)>=k and left<=right:
                psum -= nums[left]
                left+=1
            
            count += right-left + 1
        
        return count 