class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def recur(exponent):
            if 3**exponent == n:
                return True
            elif 3**exponent >n:
                return False
            return recur(exponent+1)
        return recur(0)