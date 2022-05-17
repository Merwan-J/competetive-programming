"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1,1001):
#             l,r = x,1001
            
#             while l<=r:
#                 mid = (l+r)//2
#                 result = customfunction.f(x,mid)
#                 if result==z:
#                     ans.append([x,mid])
#                 elif result < z:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
            for y in range(1,1001):
                result = customfunction.f(x,y)
                if result==z:
                    ans.append([x,y])
                    break
                elif result>z:
                    break
        return ans