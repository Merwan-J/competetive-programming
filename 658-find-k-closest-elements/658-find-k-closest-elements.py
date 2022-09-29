class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr,key=lambda item: (abs(item-x),item))
        
        return sorted(arr[:k])