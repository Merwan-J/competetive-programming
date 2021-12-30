class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        li = []
        stack = []
        if len(speed)==1:
            return 1
        
        for i in range(len(speed)):
            li.append((position[i],speed[i]))
        
        li = sorted(li,key=lambda x: x[0],reverse=True)
        for i in li:
            if len(stack)==0:
                stack.append(i)
                continue
            t1 = (target-i[0]) / i[1]
            t2 = (target - stack[-1][0]) / stack[-1][1]
            
            if t1 <= t2:
                n_t = (max(i[0],stack[-1][0]),min(i[1],stack[-1][1]))
                stack.pop(-1)
                while len(stack)!=0:
                    if (target-n_t[0]) / n_t[1] <= (target - stack[-1][0]) / stack[-1][1]:
                        stack.pop(-1)
                    else:
                        break
                stack.append(n_t)
            else:
                stack.append(i)
        return len(stack)
        
        
