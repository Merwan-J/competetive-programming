class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        [0,6,5,2,2,5,1,9,4]
    # 0  1  3 
    # 1  2  4 
    # 2  3  5
    # 3  4  6
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[i-1])
        maxTotal = -1
        l,r = 0,firstLen-1
        
        while l<=r and r<len(nums):
            crntSum = prefix[r]-prefix[l-1] if l!=0 else prefix[r]
            
            maxRight = 0
            for i in range(r+1,len(prefix)-secondLen + 1):
                maxRight = max(maxRight,prefix[i+secondLen-1]-prefix[i-1])
            
            maxLeft = 0
            if l-1-(secondLen-1)>=0:
                for j in range(0,l-secondLen+1):
                    if j==0:
                        maxLeft = max(maxLeft,prefix[secondLen-1])
                        continue
                    maxLeft = max(maxLeft,prefix[j+secondLen-1]-prefix[j-1])
            
            maxTotal = max(maxTotal,crntSum+maxLeft,crntSum+maxRight)
            
            r+=1
            l+=1
        
        return maxTotal
