class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def upperBound(l,num,upper,nums):
            r = len(nums)-1
            ans = -1 

            while l<=r:
                mid = l+(r-l)//2

                if nums[mid] + num <=upper:
                    ans = mid 
                    l = mid+1 
                else:
                    r = mid - 1
            return ans 

        def lowerBound(l,num,lower,nums):
            r = len(nums)-1
            ans = -1

            while l<=r:
                mid = l + (r-l)//2

                if nums[mid]  + num >=lower:
                    ans = mid 
                    r = mid - 1 
                else:
                    l = mid + 1 
            return ans 


        # sort the array
        nums.sort()
        count = 0 

        # iterate through the array 
        for i,num in enumerate(nums):
            # look for upperbound
            r = upperBound(i+1,num,upper,nums) 
            if r == -1:
                continue
            # look for lowerbound
            l = lowerBound(i+1,num,lower,nums)
            if l == -1:
                continue
            # increment the count
            count += r-l+1

        # return the count
        return count

            