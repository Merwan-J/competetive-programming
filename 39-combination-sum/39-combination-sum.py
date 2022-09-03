class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:       
        self.ans = []
        
        def dfs(i,total,s):
            if total == 0:
                self.ans.append(s.copy())
                return
            if total<0 or i>=len(candidates):
                return
            
            s.append(candidates[i])
            dfs(i,total-candidates[i],s)
            s.pop()
            dfs(i+1,total,s)
        
        dfs(0,target,[])
        
        return self.ans
            