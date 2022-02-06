# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n==0:
#             return x/x
#         def helper(x,n):
#             if n==1:
#                 return x
#             if n%2==0:
#                 return helper(x,n//2)**2
#             else:
#                 return x * helper(x,n//2)**2
        
#         return 1/helper(x,-n) if n<0 else helper(x,n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            x = 1/x
        if n%2 == 0:
            return self.myPow(x,n//2)**2
        return x*self.myPow(x,n//2)**2
        