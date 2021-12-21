class Solution:
    def pancakeSort(self, li: List[int]) -> List[int]:
        crnt_index = len(li)
        max_index = ''
        indices = []

        while crnt_index>=1:
            max_index = li.index(max(li[:crnt_index]))
            if max_index != crnt_index-1:
                li = li[:max_index+1][::-1] + li[max_index+1::]
                li = li[:crnt_index][::-1] + li[crnt_index:]
                indices.append(max_index+1)
                indices.append(crnt_index)
            crnt_index -= 1
        return indices 
