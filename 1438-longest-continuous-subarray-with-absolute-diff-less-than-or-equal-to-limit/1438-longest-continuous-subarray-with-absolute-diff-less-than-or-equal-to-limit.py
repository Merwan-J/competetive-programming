class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
#         what is the question?
#          - find the longest non-empty subarray diff==limit
        
#         have to track the minimum and maximum of each subarray, and the second max and second i         and so on and so forth 
        
        
        
        
#         what if I have two heaps, one for max, one for min
#         expand my window as long as their diff is less than the limit 
        
#         if the condition is not True: then shrink the window and mark the popped elt as deleted
#         and check if it is either the cur max or cur min, 
        
#         [8,2,4,7]
        
#         [8]
#         [8,2] -> [2]
        
#         [2,4,7] -> [4,7]
        
#         [8,7,2,4]
#         [7,2]
        
#         until I remove either of the extremes and replace them with extremes that results limit
        
#         what are the conditions for shrinking:
#             shrink my window to the right as long as:
#                 - I left out one of the extremes and the new formed extremes diff is less than the limit 
#         n = len(nums)
#         maxHeap = []
#         minHeap = []
#         maxSize = 0
#         deleted = set()
#         l = 0
        
#         for r in range(n):
#             heappush(maxHeap,(-nums[r],r))
#             heappush(minHeap,(nums[r],r))
            
#             # do the shrinking
#             while maxHeap and minHeap and abs(minHeap[0][0]+maxHeap[0][0])>limit:
#                 deleted.add(l)
#                 l+=1
                
#                 while maxHeap and  maxHeap[0][1] in deleted:
#                     heappop(maxHeap)
#                 while minHeap and minHeap[0][1] in deleted:
#                     heappop(minHeap)
            
#             maxSize = max(maxSize,r-l+1)
        
#         return maxSize
        

        n = len(nums)
        inc_dq = deque([])
        dec_dq = deque([])
        maxSize = 0
        l = 0
        
        for r in range(n):
            num = nums[r]
            
            # keep inc monotonicity
            while inc_dq and nums[inc_dq[-1]]>num:
                inc_dq.pop()
            # keep dec monotonicity
            while dec_dq and nums[dec_dq[-1]]<num:
                dec_dq.pop()
                
            inc_dq.append(r)
            dec_dq.append(r)
            
            # check the difference is less than or equal to limit
            while nums[dec_dq[0]]-nums[inc_dq[0]]>limit:
                l+=1
                while dec_dq[0]<l:
                    dec_dq.popleft()
                while inc_dq[0]<l:
                    inc_dq.popleft()
                    
            maxSize = max(maxSize,r-l+1)
        
        return maxSize
            
            



























