class MinStack:

    def __init__(self):
        self.li = []

    def push(self, val: int) -> None:
        self.li.append(val)

    def pop(self) -> None:
        self.li = self.li[:-1]

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return min(self.li)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
