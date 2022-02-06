class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(s,count):
            if count==n:
                return s
            inverted = ""
            for i in range(len(s)-1,-1,-1):
                if s[i]=="0":
                    inverted+="1"
                else:
                    inverted+="0"
            s = s+"1"+inverted
            return helper(s,count+1)
        return helper("0",1)[k-1]