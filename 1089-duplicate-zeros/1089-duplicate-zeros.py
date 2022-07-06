class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        longer = n + zeros
        
        l,r = n-1,longer-1
        
        while l>=0:
            if r<n:
                arr[r] = arr[l]
            if arr[l] == 0:
                r-=1
                if r<n:
                    arr[r] = arr[l]
            r-=1
            l-=1
            
        
        