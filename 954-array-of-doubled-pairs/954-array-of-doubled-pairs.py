class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort(key=lambda num: abs(num))
        seen = {}
        count = 0
        
        for num in arr:
            if num/2 in seen and seen[num/2]>0:
                seen[num/2]-=1
                count+=1
            else:
                seen[num] = seen.get(num,0) + 1

        return True if count == n/2 else False