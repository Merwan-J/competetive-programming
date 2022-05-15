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
                return ans,i
            
            if s[i]==']':
                return ans,i
            
            elif s[i]=='[':
                return helper(s,i+1,ans)
            
            elif s[i].isdigit():
                n = ''
                for j in range(i,len(s)):
                    if not s[j].isdigit():
                        break
                    n += s[j]
                    
                temp,i = helper(s,j,"")
                ans += int(n)*temp
                
                return helper(s,i+1,ans)
            
            else:
                return helper(s,i+1,ans+s[i])
        
        return helper(s,0,"")[0]
        
        
        
        
    