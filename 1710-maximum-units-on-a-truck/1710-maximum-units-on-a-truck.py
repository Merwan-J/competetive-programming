class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         count = 0
        
#         boxTypes.sort(key=lambda item: item[1])
        
#         while boxTypes and truckSize > 0:
#             boxTypes[-1][0] -= 1
#             count += boxTypes[-1][1]
#             truckSize -= 1
            
#             if boxTypes[-1][0]==0:
#                 boxTypes.pop()
            
        
#         return count
        boxes, cur_units, cnt = 0, 1000, Counter()
        for box, units in boxTypes:
            cnt[units] += box
        while cur_units > 0:
            if cnt[cur_units] > 0:
                fit_in = min(truckSize, cnt[cur_units])    
                boxes += fit_in * cur_units
                truckSize -= fit_in
                if truckSize == 0:
                    return boxes
            cur_units -= 1
        return boxes