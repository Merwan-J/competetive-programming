class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
#         def helper(arr):
#             if len(arr)==1:
#                 return arr[0]
#             return arr[-1] + helper(arr[:len(arr)-1])
        
#         res = helper(s)
        
#         for i in range(len(s)):
#             s[i] = res[i]
        
#         return s
    
        l,r = 0, len(s)-1
        
        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return s
        