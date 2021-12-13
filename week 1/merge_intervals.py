class Solution:
    def merge(self, li: List[List[int]]) -> List[List[int]]:
        intervals = li[::]
        li = sorted(li,key=lambda x: x[0])
        for i in range(len(intervals)):
            count = 0
            for i in range(len(intervals)-1):
                if i+1 < len(li) and li[i][1] >= li[i+1][0]:
                    start = li[i][0] if li[i][0] < li[i+1][0] else li[i+1][0]
                    end = li[i][1] if li[i][1] > li[i+1][1] else li[i+1][1]
                    li[i] = [start,end]

                    li.remove(li[i+1])
                    count+=1
            if count ==0:    
                return li 