class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = {}
        total = 0
        ans = []
        
        for i,num in enumerate(nums):
            if num%2==0:
                total+=num
                evens[i] = num
        
        for val,pos in queries:
            new = nums[pos] + val
            
            if pos in evens and new%2==0:
                evens[pos] = new
                total+=val
            elif pos in evens and new%2!=0:
                del evens[pos]
                total-=nums[pos]
            elif pos not in evens and new%2==0:
                evens[pos] = new
                total+=new
                
            nums[pos] = new
            ans.append(total)
            
        return ans
            
            