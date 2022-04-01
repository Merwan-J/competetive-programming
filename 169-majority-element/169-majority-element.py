class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         counter = dict()
        
#         for i in nums:
#             counter[i] = counter.get(i,0)+1
#             if counter[i]>len(nums)/2:
#                 return i

        
        candidate = -1
        votes = 0
        
        for i in nums:
            if votes==0:
                candidate = i
                votes+=1
            else:
                if candidate == i:
                    votes+=1
                else:
                    votes -=1
                    
        return candidate 
        