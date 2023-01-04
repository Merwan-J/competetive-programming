class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks).values()
        rounds = 0
        
        for count in tasks:
            if count <2:
                return -1

            if count%3 == 0:
                rounds+=count//3
            else:
                rounds+=count//3 + 1
        
        return rounds
            
        
        
        