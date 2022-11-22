class Solution:
    def numSquares(self, n: int) -> int:
#         given a number, find the least number of perfect square numbers that sum up to n
        
#         how to find the square numbers? or how to check for them?
        
#         I can pre compute which numbers are perfect or not, or I can write a function to determin that 
        
#         how to chose which perfect square to use?
        
#         I can explore every options: recursion 
#         Greedy??
        
        
#         what would the TC of the recursion be?
        
#         pick or not pick a given number -> 2^N - memo - n^2, 2 states total and current number 
        
#         1    1   1
#         2    4   3
#         3    9   5
#         4    16  7
#         5    25  9
#         6    36  11
#         7    49  13
#         8    64  15
#         9    81  17
#         10   100 19
        
#         Here the perfect squares are the prefix sum of odd numbers
        
#         what would be the states?
#         current number and total
        
#         this question can be turned into target sum problem
        
#         i can precompute and store the perfect squares in array
        
#         binary search for n in the array
        
#         find the rightful position of n
        
#         slice the array until that position and find minimum number of number combination


#         the squares length is going to be 100 at most
#         the target sum or n is going to be 10**4 at most
        
#         if I have a solution that is squareLength * n -> 10**6 which is feasible
        
        sq = [x*x for x in range(1,n) if x*x <= n]
        queue = deque([(n,1)])
        seen = set()
        seen.add(n)
        while queue:
            node, d = queue.popleft()
            if node in sq:
                return d
            for s in sq:
                if node <= s:
                    break
                if node - s not in seen:
                    seen.add(node - s)
                    queue.append((node - s, d + 1))
        return n
    
#         row = int(sqrt(n))
#         dp = [inf]*(n+1)
#         dp[0] = 0
        
#         for target in range(1,n+1):
#             for num in range(1,row+1):
#                 dp[target] = min(dp[target],1 + dp[target-num*num])
#         return dp[n]
                         
        
