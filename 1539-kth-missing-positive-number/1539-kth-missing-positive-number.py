class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
#         hset = set(arr)
#         count = 0
        
#         for num in range(1,arr[-1] + k + 2):
#             if num not in hset:
#                 count+=1
#             if count == k:
#                 return num
        
    
        def bs(l,r):
            ans = -1
            
            while l<=r:
                mid = l + (r-l)//2
                missing = arr[mid] - mid - 1
                
                if missing<k:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            return ans
        
        pos = bs(0,len(arr)-1)
        if pos == -1:
            return k
        missing = arr[pos] - pos - 1
        return arr[pos] + (k-missing)
                
            