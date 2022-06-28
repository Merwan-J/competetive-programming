class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        totalEven,totalOdd = 0,0
        evens,odds = {},{}
        
        for i in range(len(nums)):
            num  = nums[i]
            
            if i%2:
                odds[num] = odds.get(num,0)+1
                totalOdd+=1
            else:
                evens[num] = evens.get(num,0)+1
                totalEven +=1
            
        evens = sorted([(val,key) for key,val in evens.items()],reverse=True)
        odds = sorted([(val,key) for key,val in odds.items()],reverse=True)
        
        if evens[0][1]!=odds[0][1]:
            return totalEven-evens[0][0] + totalOdd-odds[0][0]
        
        ans1 = totalEven-evens[0][0] 
        ans2 = totalOdd-odds[0][0]
        
        if len(odds)==1:
            ans1+=totalOdd
        else:
            ans1+= totalOdd-odds[1][0]
        
        if len(evens)==1:
            ans2+=totalEven
        else:
            ans2+=totalEven-evens[1][0]
        
        return min(ans1,ans2)
        