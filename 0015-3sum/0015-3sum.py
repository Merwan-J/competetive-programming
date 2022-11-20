class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(num,i,ans):
            l = i+1
            r = len(nums)-1
            
            while l<r:
                if -nums[l] - nums[r] > num:
                    l+=1
                elif -nums[l] - nums[r] < num:
                    r-=1
                else:
                    ans.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    
                    while l<len(nums) and nums[l] == nums[l-1]:
                        l+=1
        
        nums.sort()
        ans = []
        
        # fix every num as i and look for j and k
        # look for j and k as what you would for the two sum, using two pointers 
        # look out for duplicates
        
        seen = set()
        
        for i, num in enumerate(nums):
            if num not in seen:
                twoSum(num,i,ans)
                seen.add(num)
        
                
        return ans