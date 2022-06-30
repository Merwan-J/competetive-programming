class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if abs(nums[i]-nums[j]) == k:
#                     count += 1
        
#         return count

#         counter = collections.defaultdict(list)
#         seen = set()
#         count = 0
        
#         for i in range(len(nums)):
#             num = nums[i]
#             counter[num].append(i)
#         for i in range(len(nums)):
#             num = nums[i]
            
#             j = -1
#             while num-k in counter and j>=-len(counter[num-k]) and counter[num-k][j]>i:
#                 count+=1
#                 j-=1
            
#             j = -1
#             while num+k in counter and j>=-len(counter[num+k]) and counter[num+k][j]>i:
#                 count+=1
#                 j-=1
            
        
#         return count

        seen = collections.defaultdict(int)
        count = 0
        
        for num in nums:
            count+=seen[num-k] + seen[num+k]
            seen[num]+=1
        return count