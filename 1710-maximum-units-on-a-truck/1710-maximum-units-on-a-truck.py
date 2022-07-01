class Solution:
    def maximumUnits(self, boxs: List[List[int]], truckSize: int) -> int:
#         boxs.sort(key=lambda box: box[1])        
#         ans = 0
        
#         while boxs and truckSize:
#             ans += boxs[-1][1]
#             boxs[-1][0]-=1
#             truckSize-=1
            
#             if boxs[-1][0] == 0:
#                 boxs.pop()
        
#         return ans


        units = collections.defaultdict(int)
        ans = 0
        
        for totalBox,unit in boxs:
            units[unit] += totalBox
        
        for cur_unit in range(1000,-1,-1):
            if units[cur_unit]>0:
                fit_in = min(truckSize,units[cur_unit])
                ans+=fit_in*cur_unit
                truckSize-=fit_in
                
                if truckSize==0:
                    return ans
            
        return ans
                