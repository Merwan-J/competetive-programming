class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        for row in mat:
            arr+=row
        
        if r*c != len(arr):
            return mat
        
        ans = [[]]
        count = 0
        for i in range(len(arr)):
            if count == c:
                ans.append([arr[i]])
                count = 1
                continue
            ans[-1].append(arr[i])
            count+=1
        
        return ans
                