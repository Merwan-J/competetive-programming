class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        pos = {index:val for index,val in enumerate(arr)}
        i = 0
        shift = 0
        
        while i<len(arr):
            arr[i] = pos[i-shift]
            if arr[i] == 0 and i+1<len(arr):
                shift+=1
                arr[i+1] = 0
                i+=1
            i+=1
        
        
        
        