class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = []
        
        def helper(count,prev,s,k,n):
            if count == n:
                self.ans.append(int(s))
                return
            
            for num in range(10):
                if abs(prev-num)==k:
                    helper(count+1,num,s+str(num),k,n)
        
        for num in range(10):
            if num!=0:
                helper(1,num,str(num),k,n)
        
        return self.ans