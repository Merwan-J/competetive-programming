class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left,right = [inf]*n,[inf]*n
        
        pos = -1
        for i in range(n):
            cur = dominoes[i]
            if cur == "R":
                pos = i
            elif cur == "L":
                pos = -1
            elif cur=="." and pos!=-1:
                right[i] = i-pos
        
        pos = -1
        for i in range(n-1,-1,-1):
            cur = dominoes[i]
            if cur == "L":
                pos = i
            elif cur == "R":
                pos = -1
            elif cur == "." and pos!=-1:
                left[i] = pos-i
        
        ans = [0]*n
        for i in range(n):
            if right[i] == left[i]:
                ans[i] = dominoes[i]
            elif right[i]<left[i]:
                ans[i] = "R"
            else:
                ans[i] = "L"
        
        return "".join(ans)
            
        
        