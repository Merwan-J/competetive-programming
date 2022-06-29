class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        ans = set()
        
        for i in range(n):
            for j in range(i+1,n):
                l,r = j+1,n-1
                total = nums[i]+nums[j]
                while l<r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total == target:
                        t = tuple(sorted([nums[i] ,nums[j] ,nums[l],nums[r]]))
                        ans.add(t)
                        l+=1
                        
                        while l<n and nums[i] == nums[i-1]:
                            l+=1
                    
                    elif total>target:
                        r-=1
                    elif total<target:
                        l+=1
        return ans                