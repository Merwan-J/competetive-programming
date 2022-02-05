class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
# the starting point of the middle subarray is [k,length-2k]

# lets find the sum of subarrays k size that start from index i[0,length-k]
#          0 1 2 3 4 5 6 7 
#       0,[1,2,1,2,6,7,5,1]
        
#         [1,3,3,3,8,13,12,6] -> sum we get from each indices considered as ending point
#         [3,3,3,8,13,12,6] -> sum we get from each indices considered as starting point 
        
#         [1,3,3,3,8,13,12,6]
#          0 1 2 3 4 5  6  7
#         [1,3,3,3,8,13,13,13]->left max of each position
#         [0,1,1,1,4,5,5,5]->positions of left max of each position
        
#         [1,3,3,3,8,13,12,6]
#          0  1  2  3  4  5  6  7 
#         [13,13,13,13,13,13,12,6]->right max of each position
#         [5,5,5,5,5,5,6,7]->position of right max of each position
        
#          0 1 2 3 4 5 6 7 
#       0,[1,2,1,2,6,7,5,1]
        
#         the middle subarray STARTING point is found in the range[k,length-2k]
#         the middle subbaray ending point is found in the range[2k-1,length-k-1]
        
#     for this testcase:
#     starting point[k,length-2k]
#     [2,4]
    
#     ----------------------------------------
#     midpoint = 2,value=3:
#     search range[0,2-k],cause we dont want to include position 1 to avoid overlapping
#     leftmax: 3 found at position 0
#     search range[midpoint+k,length-1],we dont want to include position 4 to avoid overlap
#     rightmax: 13 found at position 5
#     sum = 3+3+13=19
#     -----------------------------------------
#     midpoint = 3,value=8:
#     search range[0,3-k] and [3+k,length-1]
#     leftmax = 3 at postion 0
#     rightmax = 12 at position 5
#     sum = 8+3+12=23
#     -----------------------------------------
#     midpoint = 4,value=13
#     search range[0,4-k] and [4+k,length-1]
#     leftmax = 3 at position 0
#     rightmax = 6 at position 6
#     sum = 13+3+6=22
#     -----------------------------------------
    
#     so we take thier max sum which occurs when midpoint equals 3, [0,3,5]
# 

        ksum = [sum(nums[:k])]
        for i in range(1,len(nums)-k+1):
            ksum.append(ksum[-1]-nums[i-1]+nums[i-1+k])
        
        leftmax = [0]
        for i in range(1,len(nums)-k+1):
            getAppended = i if ksum[i] > ksum[leftmax[-1]] else leftmax[-1]
            leftmax.append(getAppended)
        print(ksum)            
        print(leftmax)
        
        rightmax = [len(nums)-k]*len(ksum)
        for i in range(len(ksum)-2,-1,-1):
            rightmax[i] = i if ksum[i]>=ksum[rightmax[i+1]] else rightmax[i+1]
        
        print(rightmax)
        print(ksum[rightmax[0]])
        
        ans = [0,0,0]
        maxSum = 0
        for i in range(k,(len(nums)-2*k+1)):
            first = leftmax[i-k]
            mid = i
            end = rightmax[i+k]
            crntSum = ksum[first]+ksum[mid]+ksum[end]
            print(first,mid,end,crntSum)
            if crntSum>maxSum:
                maxSum = crntSum
                ans = [first,mid,end]
        
        return ans
        
            
        
        
        
        
            