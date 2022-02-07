class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     arr = []
#         negatives = []
#         positives = []
        
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]<0:
#                 negatives.append(abs(nums[i]))
        
#         for i in nums:
#             if i>=0:
#                 positives.append(i)
        
#         p,n  = 0,0
        
#         while True:
#             if p<len(positives) and n<len(negatives):
#                 if positives[p]<=negatives[n]:
#                     arr.append(positives[p])
#                     p+=1
#                 else:
#                     arr.append(negatives[n])
#                     n+=1
                    
#             else:
#                 if p>=len(positives) and n>=len(negatives):
#                     break
#                 elif p>=len(positives):
#                     while n<len(negatives):
#                         arr.append(negatives[n])
#                         n+=1
#                     break
#                 elif n>=len(negatives):
#                     while p<len(positives):
#                         arr.append(positives[p])
#                         p+=1
#                     break
#         for i in range(len(nums)):
#             arr[i] = arr[i]**2
        
#         return arr
    def sortedSquares(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)