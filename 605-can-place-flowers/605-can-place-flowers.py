class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if len(flowerbed)==1 and flowerbed[0]==0:
#             return 1>=n
#         count = 0
#         i = 0
        
#         while i<len(flowerbed):
#             if flowerbed[i]==0 and i!=len(flowerbed)-1 and i!=0:
#                 if flowerbed[i+1]==flowerbed[i-1]==0:
#                     count+=1
#                     i+=1    
#             elif flowerbed[i]==1:
#                 i+=1
#             elif flowerbed[i]==0 and i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0 :
#                 count+=1
#                 i+=1
#             elif flowerbed[i]==0 and i==len(flowerbed)-1 and i-1>-1 and flowerbed[i-1]==0:
#                 count+=1
#                 i+=1
            
#             i+=1
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                empty_left = (i==0) or (flowerbed[i-1]==0)
                empty_right = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count+=1
                    if count>=n:
                        return True
        return count>=n
        
                