class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            newT = target - numbers[i]
            
            l,r = i+1,len(numbers)-1
            
            while l<=r:
                mid = l + (r-l)//2
                
                if numbers[mid] == newT:
                    return [i+1,mid+1]
                
                if numbers[mid]>newT:
                    r = mid - 1
                else:
                    l = mid + 1
            