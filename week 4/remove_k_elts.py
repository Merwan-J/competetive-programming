class Solution:
    def removeKdigits(self, li: str, k: int) -> str:
        stack = []
        if len(li) == k:
            return "0"
        for i in range(len(li)):
            while len(stack)!=0 and k>0 and int(li[i]) < int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(li[i])
        while len(stack)!=0 and k>0:
            stack.pop()
            k-=1
        ans = ''.join(stack)
        
        return "0" if stack == [] else str(int(ans))
