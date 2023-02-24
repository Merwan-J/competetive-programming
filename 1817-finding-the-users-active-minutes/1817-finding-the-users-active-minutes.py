class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0]*k
        counter = defaultdict(set)
        
        for id,time in logs:
            counter[id].add(time)
        
        for key,val in counter.items():
            ans[len(val)-1]+=1

        return ans 