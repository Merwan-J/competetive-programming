class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0

        
        is_prime = [1]*(n)
        is_prime[0] = 0
        is_prime[1] = 0
        
        
        for i in range(2,int(sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j] = 0
        return sum(is_prime)