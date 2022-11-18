class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
#         the binary search approach used in longest increasing subsequence
#         def bs(target):
#             l,r= 0,len(sub)-1
#             ans = 0
#             while l<=r:
#                 mid = l + (r-l)//2
#                 if sub[mid]>=target:
#                     ans = mid
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             return ans
        
#         sub =[]
#         for num in nums:
#             if sub==[] or num>sub[-1]:
#                 sub.append(num)
#             else:
#                 sub[bs(num)] = num
#             if len(sub) == 3: return True
        
#         return False

        first_min = inf
        second_min = inf
        
        for num in nums:
            if num<=first_min:
                first_min = num
            elif num<=second_min:
                second_min = num
            else:
                return True
        
        return False
    
        