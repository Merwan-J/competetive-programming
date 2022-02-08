class Solution:
    def countGoodNumbers(self, n: int) -> int:
        N = 1000000007
        
        def handler(power):
            if power==0:
                return 1
            res = (handler(power//2))%N
            res = (res*res)%N
            return (res*20)%N if power%2 else res
        
        res = handler(n//2)
        
        return (res*5)%N if n%2 else res
            
        
        
        
        # if n%2==0:
        #     return (pow(5,n//2,N)*pow(4,n//2,N))%N
        # else:
        #     return (pow(5,(n//2)+1,N)*pow(4,n//2,N))%N
        
    