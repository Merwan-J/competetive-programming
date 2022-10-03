class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        p1, p2 = 0, 0               
        totalCus = 0                 
        for i in range(len(customers)):
            if grumpy[i] == 0:
                totalCus += customers[i]

        cusNum = 0
        maxx = 0
        l = 0
        
        for r in range(len(customers)):
            cusNum = cusNum+customers[r] if grumpy[r] == 1 else cusNum
            while r-l + 1 == minutes:
                maxx = max(maxx,cusNum)
                cusNum = cusNum - customers[l] if grumpy[l] == 1 else cusNum
                l+=1
        
        return totalCus+maxx

