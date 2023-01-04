class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks).values()
        rounds = 0
        
        for count in tasks:
            if count <2:
                return -1
            
            if count%3 == 0 and count%2==0:
                rounds+=count//3
            elif count%3==0:
                rounds+=count//3
            else:
                rounds+=min(count//2,count//3 + 1)
        
        return rounds
            
        
        
        