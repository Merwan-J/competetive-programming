class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for m in range(k+1,n):
                        if nums[m] == nums[i]+nums[j] + nums[k]:
                            count += 1
        
        return count
        
        
        
        
        