import math
class Solution:
    def calculate(self,s):
        stack = []
        exprsn = []
        temp = ""
        for i in range(len(s)):
            if s[i] in "/-+*":
                exprsn.append(temp.strip())
                exprsn.append(s[i])
                temp=""
            else:
                if s[i] != " ":
                    temp+=s[i]
                if len(s)-1 == i:
                    exprsn.append(temp)

        for j in exprsn:
            if stack==[]:
                stack.append(int(j))
                continue
            if str(stack[-1]) in "/*":
                if stack[-1] == '*':
                    stack.pop()
                    ans = int(stack.pop()) * int(j)
                    stack.append(ans)
                else:
                    stack.pop()
                    ans = int(stack.pop()) / int(j)
                    if ans<0:
                        stack.append(math.ceil(ans))
                    else:
                        stack.append(math.floor(ans))
                continue
            elif str(stack[-1]) in "+-":
                ans = stack.pop()+j
                stack.append(int(ans))
                continue

            stack.append(j)

        return sum(stack)