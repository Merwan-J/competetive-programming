class RandomizedSet:

    def __init__(self):
        self.set = dict()
        self.keys = []
        
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            elt_2b_removed = self.set[val]
            
            if elt_2b_removed !=len(self.keys)-1:
                self.keys[elt_2b_removed] = self.keys[-1]
                self.set[self.keys[-1]] = elt_2b_removed
            
            self.keys.pop()
            self.set.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()