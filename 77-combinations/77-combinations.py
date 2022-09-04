class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        self.ans = []
        
        def dfs(i,count,n,s):
            if count == 0:
                self.ans.append(s.copy())
                return
            if i>n:
                return
            
            s.append(i)
            dfs(i+1,count-1,n,s)
            s.pop()
            dfs(i+1,count,n,s)
        
        dfs(1,k,n,[])
        
        return self.ans
            