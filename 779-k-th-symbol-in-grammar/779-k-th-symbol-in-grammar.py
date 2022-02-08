class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        
        half = 2**(n-2)
        
        if k>half:
            return 0 if self.kthGrammar(n-1,k-half)==1 else 1
        else:
            return self.kthGrammar(n-1,k)