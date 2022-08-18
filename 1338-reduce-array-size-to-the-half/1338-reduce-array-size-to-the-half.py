class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        target = n//2
        counter = collections.Counter(arr)
        counter = sorted(counter.values())
        
        count = 0
        while n>target and counter:
            n-=counter.pop()
            count+=1
        
        return count
        