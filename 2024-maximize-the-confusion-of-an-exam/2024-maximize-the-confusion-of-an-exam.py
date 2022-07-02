class Solution:
    def maxConsecutiveAnswers(self, key: str, k: int) -> int:
        char = [0,0]
        ans = 1
        
        l,r = 0,0
        while l<=r and r<len(key):
            n = r-l+1
            if key[r] == 'T':
                char[0]+=1
            else:
                char[1]+=1  
                
            moves = n-max(char)
            while moves>k:
                if key[l] == 'T':
                    char[0]-=1
                else:
                    char[1]-=1      
                n-=1
                moves = n-max(char)
                l+=1
            ans = max(ans,n)
            r+=1
            
        return ans