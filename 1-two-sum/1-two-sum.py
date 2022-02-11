class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        hashMap = dict()
        
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in hashMap and hashMap[comp]!=i:
                return [i,hashMap[comp]]
            
        
        