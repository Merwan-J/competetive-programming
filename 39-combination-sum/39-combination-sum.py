class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        path = []
        def dfs(i,total):
            if total == 0:
                ans.append(list(path))
                return
            if total<0:
                return
            
            for idx in range(i,len(candidates)):
                path.append(candidates[idx])
                dfs(idx,total-candidates[idx])
                path.pop()
        
        dfs(0,target)
        return ans