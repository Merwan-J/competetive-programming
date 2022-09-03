class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        
        
        def dfs(num,s,k,total):
            if len(s) == k and total ==0:
                self.ans.append(s.copy())
                return
            if total<0 or len(s)>k or num>9: 
                return
            s.append(num)
            dfs(num+1,s,k,total-num)
            s.pop()
            dfs(num+1,s,k,total)
        
        dfs(1,[],k,n)
        
        return self.ans
            
            
                