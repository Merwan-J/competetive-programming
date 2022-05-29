class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda item: item[1])
        heap = [(trips[0][2],trips[0][0])]
        n = capacity - trips[0][0]
        # print(trips,n)
        if n <0:
            return False
        
        for i in range(1,len(trips)):
            cur = trips[i]
            # print("round",i,"current",cur)
            if cur[0] > capacity: return False
                
            while heap and cur[1]>=heap[0][0]:
                # print(heap[0],"the min heap")
                n+=heapq.heappop(heap)[1]
            
            if n>=cur[0]:
                # print("the seat can accomodate the passegnrs")
                heapq.heappush(heap,(cur[2],cur[0]))
                n-= cur[0]
            else:
                # print("returning False")
                return False
        return True
            
                