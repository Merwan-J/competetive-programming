class Solution:
    def largestNumber(self, li):
        li = [str(i) for i in li]
        for i in range(len(li)):
            for j in range(len(li)-1):
                num = int(''.join(li))
                li[j], li[j+1] = li[j+1], li[j]
                num2 = int(''.join(li))
                if num > num2:
                    li[j], li[j+1] = li[j+1], li[j]
        li = int(''.join(li))
        return str(li)
