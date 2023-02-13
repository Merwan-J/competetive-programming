class AllOne:
    def __init__(self):
        self.d = defaultdict(int)
        self.maxq = []
        self.minq = []

    def inc(self, key: str) -> None:
        self.d[key] += 1
        heappush(self.maxq, (-self.d[key], key))
        heappush(self.minq, (self.d[key], key))
        
    def dec(self, key: str) -> None:
        self.d[key] -= 1
        if self.d[key]:
            heappush(self.maxq, (-self.d[key], key))
            heappush(self.minq, (self.d[key], key))

    def getMaxKey(self) -> str:
        while(self.maxq):
            v, k = heappop(self.maxq)
            if self.d[k] == -v:
                heappush(self.maxq, (v, k))
                return k
        return ''

    def getMinKey(self) -> str:
        while(self.minq):
            v, k = heappop(self.minq)
            if self.d[k] == v:
                heappush(self.minq, (v, k))
                return k
        return ''