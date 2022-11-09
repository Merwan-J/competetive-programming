class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        
        for i in range(n):
            psum = arr[i]
            for j in range(i+1,n):
                psum^=arr[j]
                if psum == 0:
                    count+=j-i
        
        return count
                