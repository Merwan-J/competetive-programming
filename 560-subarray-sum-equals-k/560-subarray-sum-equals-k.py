class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        sum = [nums[0]]
        count = 0
        
        for i in range(1,len(nums)):
            sum.append(sum[i-1] + nums[i])
        for i in sum:
            count+= hash.get(i-k,0)
            hash[i] = hash.get(i,0)+1
        
        return count