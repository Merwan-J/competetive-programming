class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         
       
        counter = {0:1}
        count = 0
        prefixsum  = 0
        
        for num in nums:
            prefixsum += num
            if prefixsum-k in counter:
                count+=counter[prefixsum-k]
            counter[prefixsum] = counter.get(prefixsum,0) + 1
        
        return count