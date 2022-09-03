class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        
        def dfs(i,total,s):
            if total == 0:
                self.ans.append(s.copy())
                return 
            if total<0 or i >= len(candidates):
                return
            s.append(candidates[i])
            dfs(i+1,total-candidates[i],s)
            s.pop()
            i+=1
            while i<len(candidates) and candidates[i]==candidates[i-1]:
                i+=1
            dfs(i,total,s)
        
        dfs(0,target,[])
        
        return self.ans