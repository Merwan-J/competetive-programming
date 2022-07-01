class Solution:
    def maximumUnits(self, boxs: List[List[int]], truckSize: int) -> int:
        boxs.sort(key=lambda box: box[1])        
        ans = 0
        
        while boxs and truckSize:
            ans += boxs[-1][1]
            boxs[-1][0]-=1
            truckSize-=1
            
            if boxs[-1][0] == 0:
                boxs.pop()
        
        return ans