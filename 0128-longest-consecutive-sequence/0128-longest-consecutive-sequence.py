class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ans = 0
        
        for num in nums:
            start = num
            count = 1
            while start-1 not in numsSet and num+1 in numsSet:
                numsSet.remove(num+1)
                num+=1
                count+=1
            
            ans = max(ans,count)
    
        return ans