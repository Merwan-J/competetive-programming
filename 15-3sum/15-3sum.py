class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]            
            l,r = i+1,n-1
            
            while l<r:
                total = nums[l]+nums[r]
                
                if total<target:
                    l+=1
                elif total > target:
                    r-=1
                elif total == target:
                    ans.append([-target,nums[l],nums[r]])
                    l+=1
                    while l<n and nums[l] == nums[l-1]:
                        l+=1
        
        return ans