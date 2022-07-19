class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 1 2 3 4 5
        
        
        # nums = [i+1 for i in range(1000)]
        # print(nums)
        count = collections.Counter(nums)
        
        nums = list(set(nums))
        nums.sort()
        
        @cache
        def dfs(i, picked):
            if i==len(nums):
                # print(p)
                return 0
            
            num = nums[i]
            t = num*count[num] 

            yes = 0 if picked and (nums[i-1]+1==num) else t+ dfs(i+1, True)
            no = dfs(i+1, False)
            
            return max(yes, no)
        
        return dfs(0, False)
    
#         ans = -1
        
#         for num in nums:
#             ans = max(ans,t)
        
#         return ans
    
         