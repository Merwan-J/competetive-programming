class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        self.check = set(self.heap)
        pointer = 1001
        

    def popSmallest(self) -> int:
        if len(self.heap)>0:
            ans = heapq.heappop(self.heap)
            self.check.remove(ans)
        else:
            ans = self.pointer
            self.pointer+=1
        
        return ans

    def addBack(self, num: int) -> None:
        if num not in self.check:
            heapq.heappush(self.heap,num)
            self.check.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)



# I will have a heap that contains numbers from 1-1000
# I will have a pointer that will point at numbers beyond 1000, i.e starting from 1001 
# I will also have a member array of size 1001 where array[i] = 1 if it is already in the set else it will be 0 

# the idea is to pop from the heap until it is empty. if it is empty return the pointer and increment it 