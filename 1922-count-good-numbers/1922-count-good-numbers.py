class Solution:
    def countGoodNumbers(self, n: int) -> int:
        N = 1000000007
        # five = pow(5,)
        # def helper(n):
        #     if n==
        if n%2==0:
            return (pow(5,n//2,N)*pow(4,n//2,N))%N
        else:
            return (pow(5,(n//2)+1,N)*pow(4,n//2,N))%N
        
    