class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
#         self.ans = ""
        
#         def dp(i,j,a,b,s):
#             if a >= 3 or b>=3:
#                 return
            
#             if i<0 or j<0:
#                 return
            
#             if i == 0 and j == 0:
#                 self.ans = s
#                 return
            
#             dp(i-1,j,a+1,0,s+"a")
#             if self.ans != "": return
#             dp(i,j-1,0,b+1,s+"b")

            
            
            
#         dp(a,b,0,0,"")
#         return self.ans
        
    
        s = ""
        
        while a + b>0:
            c = 0
            while a >0 and a>=b and c<2:
                a-=1
                c+=1
                s+="a"
                if c == 2 and a>b:
                    c = 0
                    s+="b"
                    b-=1
            
            c = 0
            while b>0 and b>=a and c<2:
                b-=1
                c+=1
                s+="b"
                if c == 2 and b>1:
                    c = 0
                    s+="a"
                    a-=1
                
            
        return s
                
                
                
            
        
                