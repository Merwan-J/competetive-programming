class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        stop = set(deadends)
        q = deque(["0000"])
        visited = set()
        level = 0
        
        
        while q:
            n  = len(q)
            for _ in range(n):
                s = q.popleft()

                if s in stop or s in visited:
                    continue

                if s == target:
                    return level

                visited.add(s)

                s = [i for i in s]

                for i in range(4):
                    up = int(s[i]) + 1
                    down = int(s[i]) - 1

                    if up == 10: up = 0
                    if down == -1: down = 9
                    
                    temp = s[i]
                    s[i] = str(up)
                    q.append("".join(s))
                    s[i] = str(down)
                    q.append("".join(s))
                    s[i] = temp
            level+=1
        return -1 
            
            
                
                
                
            
            
            
            
        
        
        
        