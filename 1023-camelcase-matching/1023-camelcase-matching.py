class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n  = len(pattern)
        ans = [False]*len(queries)
        
        for j in range(len(ans)):
            word = queries[j]
            i = 0
            add = True
            
            for char in word:
                # print(char,i,pattern)
                if char.isupper():
                    if i<n and char == pattern[i]:
                        i+=1
                    else:
                        add = False
                        break
                elif char.islower():
                    if i<n and char == pattern[i]:
                        i+=1
                
            if i==n and add:
                ans[j] = True        
                
        
        return ans