class Solution:
    def findMin(self, nums: List[int]) -> int:
#         [1, 2, 3, 4, 5] -> original array
#          0  1  2  3  4 
#         [4, 5, 1, 2, 3] -> rotated array at index 2
        
#         -> left most and right most element are greater than or equal to the minimum elt
#         -> left most elt is greater than or equal to the right most elt
#       => greater part and smaller part
#       greater part=> mid >= leftmost elt and mid>= rightmost elt
#       smaller part => mid<= leftmost elt  and mid <= rightmost elt
        l,r = 0, len(nums)-1
        pivot = 0
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid]>= nums[0] and nums[mid]>=nums[-1]:
                l = mid + 1 
            elif nums[mid] <= nums[0] and nums[mid] <= nums[-1]:
                pivot = mid
                r = mid - 1
            else:
                break
        
        return nums[pivot]
        
        
            
            
        