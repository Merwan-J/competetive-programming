class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(arr,start,end):
            mid = start + (end-start+1)//2
            if start>end:
                return 0
            
            if start==end:
                if arr[start]<0:
                    return len(arr)-start
                return 0
            if arr[mid]>=0:
                return search(arr,mid+1,end)
            else:
                if arr[mid-1]<0:
                    return search(arr,start,mid-1)
                return len(arr)-mid
        
        count = 0
        for mat in grid:
            x = search(mat,0,len(mat)-1)
            # print(x)
            count+=x
        return count
            