class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
#         1,2,3,4,5,6   limit = 6
        if len(people)==1:
            return 1
        
        people.sort()
    
        l,r = 0,len(people)-1
        count = 0
        
        while l<=r:
            if people[l]+people[r] <= limit:
                l+=1
                
            count+=1
            r-=1
                
        return count