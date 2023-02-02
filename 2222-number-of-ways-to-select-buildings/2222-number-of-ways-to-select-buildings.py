class Solution:
    def numberOfWays(self, s: str) -> int:
        ans=0
        n=len(s)
        left=[0]*n
        right=[0]*n
        zeros,ones=0,0
        
        for i in range(n):
            if s[i]=="0": 
                zeros+=1
                left[i]=ones
            else: 
                ones+=1
                left[i]=zeros
                
        zeros,ones=0,0
        for i in range(n-1,-1,-1):
            if s[i]=="0": 
                zeros+=1
                right[i]=ones
            else: 
                ones+=1
                right[i]=zeros
                
            ans+=left[i]*right[i]
            
        return ans