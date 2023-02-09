class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        p, q, max_i = -1, -1, len(digits)-1
        
        for i in range(max_i-1, -1, -1):
            if digits[i] > digits[max_i]:
                max_i = i
            elif digits[i] < digits[max_i]:
                p, q = i, max_i

        if p > -1:
            digits[p], digits[q] = digits[q], digits[p]
            
        return int(''.join(digits))