class Solution:
    def maxFrequency(self, li: List[int], k: int) -> int:
        li.sort()
        start,end,sum  = 0,0,0
        count = 1
        for i in range(len(li)):
            sum += li[end]
            length = end-start + 1
            if length*li[end] - sum <= k:
                if length > count:
                    count += 1
            else:
                sum -= li[start]
                start += 1
            end +=1
        return count

    