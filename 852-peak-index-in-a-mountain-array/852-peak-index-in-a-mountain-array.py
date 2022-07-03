class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         for i in range(1,len(arr)-1):
#             if arr[i]>arr[i+1]:
#                 return i
        
        l,r = 1,len(arr)-2
        
        while l<=r:
            mid = l + (r-l)//2
            
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            
            if arr[mid]<=arr[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        