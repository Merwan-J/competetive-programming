class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hmap = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        
        index = self.hmap[val]
        lastNum = self.arr[-1]
        n = len(self.arr)-1
        
        self.arr[index] = lastNum
        self.arr.pop()
        
        del self.hmap[val]
        
        if lastNum != val:
            self.hmap[lastNum] = index
        return True

    def getRandom(self) -> int:
        return self.arr[randint(0,len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()