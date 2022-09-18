class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i>=len(questions):
                return 0
            solve = questions[i][0] + dfs(i+1+questions[i][1])
            skip = dfs(i+1)
            
            return max(solve,skip)
        
        return dfs(0)