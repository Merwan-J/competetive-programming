class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [] 
        path = []
        
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return 
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        
        dfs(0)
        
        return ans 