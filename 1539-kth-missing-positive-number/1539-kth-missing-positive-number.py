class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        hset = set(arr)
        count = 0
        
        for num in range(1,arr[-1] + k + 2):
            if num not in hset:
                count+=1
            if count == k:
                return num
        
            