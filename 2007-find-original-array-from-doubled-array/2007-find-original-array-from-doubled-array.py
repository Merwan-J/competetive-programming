class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr.sort()
        seen = {}
        ans = []
        
        for num in arr:
            if num/2 in seen and seen[num/2]>0:
                ans.append(num//2)
                seen[num/2]-=1
            else:
                seen[num] = seen.get(num,0) + 1
            
        return ans[:n//2] if len(ans)==n/2 else []
        