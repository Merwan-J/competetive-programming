class Solution:
    def decodeString(self, s: str) -> str:
#         stack = []
        
#         for i in s:
#             if i != ']':
#                 stack.append(i)
#             else:
#                 temp = ""
#                 n = ""
                
#                 while stack[-1] != '[':
#                     temp = stack.pop() + temp
                    
#                 stack.pop()
                
#                 while stack and stack[-1].isdigit():
#                     n = stack.pop() + n
                
#                 stack.append(int(n)*temp)
            
#         return "".join(stack)
        
    
#     3 [ a ] 2 [ b c ]
#     0 1 2 3 4 5 6 7 8
    
#     -> 3 * helper(2,"") = "aaa"
#         -> helper(4,"aaa")
#             -> 2 * helper(6,"") = "bcbcbc"
#                 -> helper(9,"aaabcbc")
    
    
    
    
    
    
        def helper(s,i,ans):
            if i>= len(s):
                print("shit is over")
                return ans,i
            
            if s[i]==']':
                print("brace closed")
                return ans,i
            
            elif s[i]=='[':
                print("it is opening brace")
                return helper(s,i+1,ans)
            elif s[i].isdigit():
                print(s[i])
                n = ''
                
                for j in range(i,len(s)):
                    if not s[j].isdigit():
                        break
                    n += s[j]
                print(n,"its a digit")
                temp,i = helper(s,j,"")
                print(temp,i,"multilpy this shit with",n)
                ans += int(n)*temp
                return helper(s,i+1,ans)
            
            else:
                print(s[i],"just a letter, append it")
                return helper(s,i+1,ans+s[i])
        
        return helper(s,0,"")[0]
        
        
        
        
    