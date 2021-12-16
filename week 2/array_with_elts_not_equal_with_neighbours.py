class Solution:
    def rearrangeArray(self, li: List[int]) -> List[int]:
        for i in range(len(li)):
            count = 0
            for j in range(1,len(li)-1):
                l = li[j-1]
                r = li[j+1]
                a = (l+r)/2
                
                if li[j] == a:
                    li[j-1],li[j] = li[j],li[j-1]
                    count+=1
            if count == 0:
                return li
    