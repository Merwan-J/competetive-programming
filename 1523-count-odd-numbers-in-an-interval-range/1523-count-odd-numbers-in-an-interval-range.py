class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high-low + 1
        
        if total%2 == 0:
            return total//2
        
        return total//2 if low%2==0 else total - total//2 