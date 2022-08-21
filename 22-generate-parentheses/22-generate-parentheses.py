class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def generate(o,c,s):
            if c<o:
                return
            
            if o == 0:
                for i in range(c):
                    s+=")"
                self.ans.append(s)
                return
            
            generate(o-1,c,s+"(")
            generate(o,c-1,s+")")
            
        
        generate(n,n,"")
        return self.ans
        