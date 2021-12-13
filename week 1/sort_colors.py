class Solution:
    def sortColors(self, li: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(li)):
            crnt_value = li[i]
            crnt_index = i
            for j in range(len(li)):
                compare_index = crnt_index - 1

                if crnt_value < li[compare_index]:
                    li[crnt_index] = li[compare_index]
                    li[compare_index] = crnt_value
                    crnt_index -= 1
                    compare_index -= 1

                if compare_index == -1 or crnt_value > li[compare_index]:
                    break