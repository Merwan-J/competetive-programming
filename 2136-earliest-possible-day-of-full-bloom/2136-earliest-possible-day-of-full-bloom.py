class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = sorted(zip(growTime, plantTime), reverse=True)
        
        curPlantTime = 0
        curTargetTime = 0
        
        for grow, plant in times:
            curPlantTime += plant
            curTargetTime = max(curTargetTime, curPlantTime + grow)
        
        return curTargetTime  