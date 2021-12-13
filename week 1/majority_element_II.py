class Solution:
    def majorityElement(self, li: List[int]) -> List[int]:
        new_li = []
        n = len(li)/3
#         I know I could have used count() so shut up!
        for i in set(li):
            count = 0
            for j in li:
                if i == j:
                    count+=1
            if count > n:
                new_li.append(i)
        return new_li
