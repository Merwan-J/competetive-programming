class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        seen = set()
        stack = []
        i = 0
        
        while i<len(s):
            cur = s[i]
            while stack and cur not in seen and cur<stack[-1] and counter[stack[-1]] > 0 :
                seen.remove(stack.pop())
                    
            if cur not in seen: 
                stack.append(cur)
                seen.add(cur)
            counter[cur] -= 1
            
            i+=1
        
        return ''.join(stack)
        
        
        
                