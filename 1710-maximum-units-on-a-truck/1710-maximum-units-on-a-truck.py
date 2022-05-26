class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        
        boxTypes.sort(key=lambda item: item[1])
        
        while boxTypes and truckSize > 0:
            boxTypes[-1][0] -= 1
            count += boxTypes[-1][1]
            truckSize -= 1
            
            if boxTypes[-1][0]==0:
                boxTypes.pop()
            
        
        return count