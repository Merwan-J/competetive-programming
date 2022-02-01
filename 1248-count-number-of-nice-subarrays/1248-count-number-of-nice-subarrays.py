class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        """

        

        
        """
        
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        
        prefix = 0
        hashMap = {0:1}
        count = 0
        
        for num in nums:
            prefix +=num
            count += hashMap.get(prefix-k,0)
            hashMap[prefix] = hashMap.get(prefix,0)+1
        
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        while r<len(nums):
            if nums[r]%2!=0:
                odds+=1
                print("it is odd and counted")
            elif nums[r]%2==0:
                print("it is even doesnt matter")
                r+=1
                continue
            
            if odds>k:
                print("greater than the limit")
                while odds>k:
                    if nums[l]%2!=0:
                        odds-=1
                    l+=1
            if odds==k:
                print("found it")
                count+=1
            r+=1
        return count
            