class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def dfs(cur):
            if cur == len(nums):
                ans.append(path.copy())
                return 
            
            path.append(nums[cur])
            dfs(cur+1)
            path.pop()
            prev = cur
            cur+=1
            while cur<len(nums) and nums[cur] == nums[prev]:
                cur+=1
            dfs(cur)
            
        dfs(0)
        return ans