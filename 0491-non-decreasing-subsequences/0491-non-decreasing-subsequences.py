class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        
#         we have nums and we have to find non decreasing sub seq. 
        
#         since sub seq is the result of deletion of zero or more elts from the array and the resulting seq has also to keep the original order
        
#         by deleting means: we can include the elt of the array in the sub or not 
            
#         we have to choice for each of th elt: pick or not pick
            
            
        
        def dfs(i,path):
            if i == len(nums):
                if len(path)>1:
                    ans.append(tuple(path))
                return
            
            
            if not path or (path and nums[i]>=path[-1]):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,path)
        
        ans = []

        dfs(0,[])
        
        return set(ans)
            
            
                
                