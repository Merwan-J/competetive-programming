class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        i = 0
        
        while i<n-2 and nums[i]<1:
            j,k = i+1,n-1
            
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    
                    while j<n and nums[j] == nums[j-1]:
                        j+=1
                    
                    while k>i and nums[k] == nums[k+1]:
                        k-=1
                elif total<0:
                    j+=1
                else:
                    k-=1
            i+=1
            
            while i<n and nums[i] == nums[i-1]:
                i+=1
                
            
        return ans 
                    

        
        [-1,-1,0,1]
                        