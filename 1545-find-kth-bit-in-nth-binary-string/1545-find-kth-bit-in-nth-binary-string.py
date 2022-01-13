class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(s,i):
            crnt = s + '1' 
            inv_str = ''
            for l in range(len(s)):
                if s[l] == '0':
                    inv_str += "1"
                else:
                    inv_str += "0"
                    
            s = crnt + "".join(inv_str[::-1])
            if i == n:
                return s
            return recur(s,i+1)
        
        return recur("0",1)[k-1]