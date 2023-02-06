class DetectSquares:

    def __init__(self):
        self.vertical_points = collections.defaultdict(set)
        self.counter = collections.defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        
        x,y = point
        self.vertical_points[x].add(y)
        self.counter[(x,y)]+=1
        
    def count(self, point: List[int]) -> int:
        x1,y1 = point 
        ans = 0
        for y in self.vertical_points[x1]:            
            x2,y2 =x1,y            
            side =abs(y-y1)
            
            if side<1: continue
            x3,y3 = x1-side,y1
            x4,y4 = x1-side,y2
            
            ans += self.counter[(x2,y2)]*self.counter[(x3,y3)]*self.counter[(x4,y4)]
            
            x3,y3= x1+side,y1
            x4,y4 = x1+side,y2
            
            ans += self.counter[(x2,y2)]*self.counter[(x3,y3)]*self.counter[(x4,y4)]
            
        return ans