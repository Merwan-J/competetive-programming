from bisect import bisect_left

class Solution:
    def __init__(self, w: List[int]):
        self.weights = [0.0] * len(w)
        s, cur = sum(w), 0.0
        for i, wgt in enumerate(w):
            cur += float(wgt) / s
            self.weights[i] = cur
        
    def pickIndex(self) -> int:
        return bisect_left(self.weights, random.random())
    
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()