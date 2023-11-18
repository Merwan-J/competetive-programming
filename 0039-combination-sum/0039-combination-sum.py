class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        ans = []
        path = [] 
        
        def dfs(i,total):
            if total == 0:
                ans.append(path[:])
                return 
            
            if i == len(candidates) or candidates[i]>total:
                return 
            
            path.append(candidates[i])
            dfs(i,total-candidates[i])
            path.pop()
            dfs(i+1,total)
        
        dfs(0,target)
        
        return ans 