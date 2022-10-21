class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.hmap = defaultdict(set)

    def insert(self, val: int) -> bool:
        # print(self.arr,"before inserting")
        self.arr.append(val)
        self.hmap[val].add(len(self.arr)-1)
        # print(self.arr,"after inserting",len(self.hmap[val]) == 1)
        return len(self.hmap[val]) == 1

    def remove(self, val: int) -> bool:
        # print(self.hmap[val],len(self.hmap[val]),"checking")
        if len(self.hmap[val]) == 0:
            return False
        # print(self.arr,"before removing",val,self.hmap)
        index = self.hmap[val].pop()        
        lastNum = self.arr[-1]
        n = len(self.arr)
        
        self.arr[index] = lastNum
        self.arr.pop()
        
        self.hmap[lastNum].discard(n-1)
        if index != n-1:
            self.hmap[lastNum].add(index)
        # print(self.arr,"after removing",self.hmap)
        return True
    
    def getRandom(self) -> int:
        start = 0
        end = len(self.arr)-1
        # print(start,end,self.arr)
        index = random.randint(start,end)
        return self.arr[index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()