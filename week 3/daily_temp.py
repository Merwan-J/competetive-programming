class Solution:
    def dailyTemperatures(self, li: List[int]) -> List[int]:
        stack = []
        d = {}

        for i in range(len(li)):
            if i==0:
                stack.append((li[i],i))
            if li[i] > stack[-1][0]:
                d[stack[-1][1]] = i-stack[-1][1]
                stack.pop(-1)
                while len(stack) != 0:
                    if stack[-1][0]< li[i]:

                        d[stack[-1][1]] = i-stack[-1][1]
                        stack.pop(-1)
                    else:
                        break
                stack.append((li[i],i))

            elif li[i] <= stack[-1][0]:
                stack.append((li[i],i))

        arr = []
        for i in range(len(li)):
            if i not in d:
                arr.append(0)
            else:
                arr.append(d[i])

        return arr
