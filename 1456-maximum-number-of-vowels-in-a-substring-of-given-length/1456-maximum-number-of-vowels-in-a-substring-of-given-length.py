class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o','u'])
        
        l = 0
        count = 0 
        ans = 0 
        
        for r,char in enumerate(s):
            if char in vowels: count+=1
            
            if r-l+1>k:
                if s[l] in vowels: 
                    count-=1
                l+=1 
                    
                
            ans = max(ans,count)
        
        return ans 