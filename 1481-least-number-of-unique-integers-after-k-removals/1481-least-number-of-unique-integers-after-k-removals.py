class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        Map = dict()
        
        for num in arr:
            Map[num] = Map.get(num,0)+1
        
        Map = dict(sorted(Map.items(),key=lambda item: item[1]))
        
        for num in Map:
            if Map[num]>0 and k>0:
                count = Map[num]
                Map[num] = 0 if k>=count else count - k
                k -= count - Map[num]
        
        count = 0
        for num in Map:
            if Map[num]>0:
                count+=1
        return count