class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        [0,6,5,2,2,5,1,9,4]
    # 0  1  3 
    # 1  2  4 
    # 2  3  5
    # 3  4  6
        l,r = 0,firstLen
        
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(nums[i]+prefixSum[-1])
        # print(prefixSum)
        # [0, 0, 6, 11, 13, 15, 20, 21, 30, 34]

        MaxSum = 0 
        while r<=len(nums):
            crntSum = prefixSum[r]-prefixSum[l]
            # print(crntSum)
            
            maxRight = 0
            for i in range(r,len(nums)-secondLen+1):
                maxRight = max(maxRight,prefixSum[i+secondLen]-prefixSum[i])
                
            maxLeft = 0
            for i in range(0,l-secondLen+1):
                maxLeft = max(maxLeft,prefixSum[i+secondLen]-prefixSum[i])
            MaxSum = max(MaxSum,crntSum + max(maxLeft,maxRight))
            
            l+=1
            r+=1
        
        return MaxSum

    