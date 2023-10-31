class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s,t = 0,0
        n = len(start)
        
        while s<n or t<n:
            while s<n and start[s] == "_":
                s+=1
            while t<n and target[t] == "_":
                t+=1 
            
            if s == n or t == n or start[s]!=target[t] or (start[s] == "L" and s<t) or (start[s]=="R" and s>t):
                break 
            
            s+=1
            t+=1
        
        return t == n and s == n 
    
    
        
        
        
        