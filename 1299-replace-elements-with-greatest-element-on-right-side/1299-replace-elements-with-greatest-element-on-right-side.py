class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        prev = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            mx = max(prev,mx)
            prev = arr[i]
            arr[i] = mx
        arr[-1] = -1
        
        return arr