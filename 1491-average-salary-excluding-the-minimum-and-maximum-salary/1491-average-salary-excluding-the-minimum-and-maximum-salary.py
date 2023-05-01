class Solution:
    def average(self, salary: List[int]) -> float:
        mn = salary[0]
        mx = salary[0]
        total = 0
        
        for s in salary:
            total+=s 
            mn = min(mn,s)
            mx = max(mx,s)

        return (total - mn - mx)/(len(salary)-2)