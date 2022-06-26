class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a,b = nums.index(min(nums)),nums.index(max(nums))
        if a>b:
            a,b = b,a
        return min(b+1,len(nums)-a,a+1+len(nums)-b)
    