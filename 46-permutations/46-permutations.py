class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        ans,path = [],[]
        
        def dfs():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs()
                    path.pop()
        
        
        dfs()
        return ans