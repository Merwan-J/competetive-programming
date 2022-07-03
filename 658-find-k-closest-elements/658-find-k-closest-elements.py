class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r  = 0,len(arr)-1
        
        while (r-l+1)>k:
            if abs(arr[l]-x)<=abs(arr[r]-x):
                r-=1
            else:
                l+=1
        
        return arr[l:r+1]
    