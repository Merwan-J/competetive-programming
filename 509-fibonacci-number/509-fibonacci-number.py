class Solution:
    def fib(self,n):
        memo = [None]*(n+1)
        def helper(n,m):
            print(n)
            if memo[n] is not None:
                return memo[n]

            if n==1 or n==2:
                result = 1
            elif n==0:
                return 0
            else:
                result = helper(n-1,memo) + helper(n-2,memo)

            memo[n] = result 
            return result
        return helper(n,memo)
    
    