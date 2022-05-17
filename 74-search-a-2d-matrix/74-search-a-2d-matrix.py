class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for li in matrix:
            l,r = 0,len(li)-1
            while l<=r:
                mid = (l+r)//2
                if li[mid] == target:
                    return True
                if li[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1 
                    
        return False