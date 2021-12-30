class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.li = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.li = [value]+self.li
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.li.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.li.pop(0)
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.li.pop(-1)
        return True

    def getFront(self) -> int:
        return self.li[0] if len(self.li) != 0 else -1

    def getRear(self) -> int:
        return self.li[-1] if len(self.li) != 0 else -1

    def isEmpty(self) -> bool:
        return len(self.li) == 0

    def isFull(self) -> bool:
        return len(self.li) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()