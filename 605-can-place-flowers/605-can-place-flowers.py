class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            return 1>=n
        count = 0
        i = 0
        
        while i<len(flowerbed):
            if flowerbed[i]==0 and i!=len(flowerbed)-1 and i!=0:
                if flowerbed[i+1]==flowerbed[i-1]==0:
                    # print("possible",i,flowerbed)
                    count+=1
                    i+=1
                # else:
                    # print("not possibele",i,flowerbed)
                    
            elif flowerbed[i]==1:
                # print("not possible",i,flowerbed)
                i+=1
            elif flowerbed[i]==0 and i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0 :
                # print("possible",i,flowerbed)
                count+=1
                i+=1
            elif flowerbed[i]==0 and i==len(flowerbed)-1 and i-1>-1 and flowerbed[i-1]==0:
                # print("possible",i,flowerbed)
                count+=1
                i+=1
            
            i+=1
        
        return count>=n
                