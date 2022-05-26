class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = [(capacity[i]-rocks[i]) for i in range(len(rocks))]
        
        bags.sort()
        
        for i in range(len(bags)):
            if bags[i]>0 and additionalRocks > 0:
                dcr = min(bags[i],additionalRocks)
                bags[i] -= dcr 
                additionalRocks -= dcr
            
            if additionalRocks == 0:
                break
        count = 0
        
        for i in bags:
            if i == 0:
                count += 1
            else:
                return count
        return count
        