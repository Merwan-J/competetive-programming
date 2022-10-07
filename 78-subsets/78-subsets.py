class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i,path):
            if i == len(nums):
                ans.append(path)
                return
            
            dfs(i+1,path)
            dfs(i+1,path+[nums[i]])
            
        dfs(0,[])    
        return ans
    
    