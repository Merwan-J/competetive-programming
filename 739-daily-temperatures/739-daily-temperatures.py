class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0]*len(temperatures)
        
        for i,num in enumerate(temperatures):
            while stack and stack[-1][0]<num:
                pos = stack.pop()[1]
                ans[pos] = i-pos
            
            stack.append((num,i))
        
        return ans