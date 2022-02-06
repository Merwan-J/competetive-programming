class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return x/x
        def helper(x,n):
            if n==1:
                return x
            res = helper(x*x,n//2)
            return x * res if n%2 else res
        
        return 1/helper(x,-n) if n<0 else helper(x,n)



        