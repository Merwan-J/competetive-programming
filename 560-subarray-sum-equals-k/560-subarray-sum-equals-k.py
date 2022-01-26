class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        count = 0
        prefixSum = 0
        
        for i in nums:
            prefixSum+=i
            count+= hash.get(prefixSum-k,0)
            hash[prefixSum] = hash.get(prefixSum,0)+1
        
        return count