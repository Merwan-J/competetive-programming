class MinStack:

    def __init__(self):
        self.li = []

    def push(self, val: int) -> None:
        if self.li==[]:
            self.li.append((val,val))
            return None
        self.li.append((val,min(self.li[-1][1],val)))

    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return self.li[-1][0]

    def getMin(self) -> int:
        return self.li[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()