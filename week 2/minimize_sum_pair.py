class Solution:
    def minPairSum(self, li: List[int]) -> int:
        li = sorted(li,reverse=True)
        start = 0
        end = len(li)-1
        arr = []
        while start<=end:
            arr.append(li[start]+li[end])
            start+=1
            end-=1
        return max(arr)
