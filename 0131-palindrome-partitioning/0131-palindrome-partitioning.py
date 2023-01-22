class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def checkPalindrome(s):
            l,r = 0,len(s)-1
            
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
                
            return True
    
        
        def separate(i,path):
            if i>=len(s):
                ans.append(path.copy())
                return
            
            for j in range(i+1,len(s)+1):
                newString = s[i:j]
                if checkPalindrome(newString):
                    path.append(newString)
                    separate(j,path)
                    path.pop()
        
        ans = []
        separate(0,[])
        
        return ans
            