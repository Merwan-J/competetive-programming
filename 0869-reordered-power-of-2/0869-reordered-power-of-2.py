class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sorted_N_str = sorted(str(n))

        maximum = 10 ** 9
        i = 1

        while i <= maximum:
            sorted_i_str = sorted(str(i))
            if sorted_i_str == sorted_N_str:
                return True
            i = i * 2
        
        return False