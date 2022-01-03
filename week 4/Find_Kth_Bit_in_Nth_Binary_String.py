class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(s,i):
            crnt = s + '1' 
            s = [j for j in s]
            for l in range(len(s)):
                s[l] = "0" if s[l]=="1" else "1"
            s = crnt + "".join(s[::-1])
            
            if i == n:
                return s
            return recur(s,i+1)
        
        return recur("0",1)[k-1]
