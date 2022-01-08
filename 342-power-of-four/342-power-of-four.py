class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recur(exponent):
            if 4**exponent == n:
                return True
            elif 4**exponent >n:
                return False
            return recur(exponent+1)
        return recur(0)