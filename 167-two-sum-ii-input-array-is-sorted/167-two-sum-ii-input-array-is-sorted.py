class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = dict()
        
        for i in range(len(numbers)):
            if target-numbers[i] in hash:
                return [hash[target-numbers[i]]+1,i+1]
            hash[numbers[i]] = i
        
        
#         l,r = 0, len(numbers)-1
        
#         while l<r:
#             sum = numbers[l] + numbers[r]
#             if sum == target:
#                 return [l+1,r+1]
#             elif sum < target:
#                 l+=1
#             else:
#                 r-=1