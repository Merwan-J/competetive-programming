class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height)==2:
            return 0
        
        l, r, total = 0, 1, 0
        stack = []  
        monotone = []
        while l < len(height)-2:
            if height[l] == 0:
                l+=1
                r = l+1
                stack = []
                monotone = []
                continue 
                
            if height[r] >= height[l]:
                while stack:
                    total += min(height[l],height[r]) - stack[-1]
                    stack.pop()
                l = r
                r = r+1
                monotone = []
                stack = []
                continue  
            if r>= len(height)-1:
                stack.append(height[r])
                monotone.append(r)
                l+=1
                r = l+1
                
                rMax = max(stack)
                index = stack.index(rMax)
                if index != 0:
                    for i in range(index):
                        total += rMax-stack[i]
                    l = monotone[index]
                    r = l+1
               
                stack = []
                monotone = []
                continue
            monotone.append(r)
            stack.append(height[r])
            r+=1
        return total