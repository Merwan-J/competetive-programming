class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(num2)):
            if len(stack)==0:
                stack.append(num2[i])
                continue
            if stack[-1] < num2[i]:
                d[stack[-1]] = num2[i]
                stack.pop(-1)
                while len(stack) != 0:
                    if stack[-1]< num2[i]:
                        d[stack[-1]] = num2[i]
                        stack.pop(-1)
                    else:
                        break
                stack.append(num2[i])
            elif stack[-1] > num2[i]:
                stack.append(num2[i])
        li = []
        for i in num1:
            if i in d:
                li.append(d[i])
            else:
                li.append(-1)


        return li
