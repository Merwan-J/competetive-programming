class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
#         1,2,3,4,5,6   limit = 6
        count = 0
        people.sort()
        
        l,r = 0,len(people)-1
        
        while l<=r:
            sum = people[l]+people[r]
            if sum<=limit:
                l+=1
            count+=1
            r-=1
            
        return count