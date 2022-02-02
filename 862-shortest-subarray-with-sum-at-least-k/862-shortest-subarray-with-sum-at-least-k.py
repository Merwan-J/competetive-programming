from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
#        Stack(technically a deque) will be used to store the prefix sum monotonically
#        for each iteration we chech for target and if it is greater or equal to target 
#       compare the current size with the stored min size
# append to the deque

        stack = deque([])
        total = 0
        size = len(nums)+1
        l,r = 0,0
        
        while l<=r and r<len(nums):
            total += nums[r]
            
            if total>=k:
                size = min(size,r-l+1)
            
            while stack and stack[-1][0]>total:
                stack.pop()
            
            stack.append((total,r))
            
            while stack and stack[-1][0]-stack[0][0] >=k:
                l = stack[0][1] + 1
                stack.popleft()[0]
                size = min(size,r-l+1)
            
            r+=1
                
                
        return -1 if size == len(nums)+1 else size
            
            
        
            
        
                
                
        