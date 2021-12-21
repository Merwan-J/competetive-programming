class MyQueue:

    def __init__(self):
        self.li = []

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        el = self.li[0]
        self.li.remove(self.li[0])
        return el

    def peek(self) -> int:
        return self.li[0]

    def empty(self) -> bool:
        return len(self.li) == 0     
