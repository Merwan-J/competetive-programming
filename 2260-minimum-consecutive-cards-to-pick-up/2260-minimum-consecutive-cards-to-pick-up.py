class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        values = dict()
        ans = len(cards)+1
        
        for i in range(len(cards)):
            val = cards[i]
            if val in values:
                ans = min(ans,i-values[val]+1)
            values[val] = i
        
        return ans if ans<len(cards)+1 else -1

            