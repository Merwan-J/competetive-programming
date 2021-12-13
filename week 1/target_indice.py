class Solution:
    def counting_sort(self,li):
        new_li = [0 * i for i in range(max(li)+1)]
        for i in set(li):
            count = li.count(i)
            new_li[i] = count

        an_li = []
        for j in range(len(new_li)):
            for k in range(new_li[j]):
                an_li.append(j)
        return an_li
    def targetIndices(self,li,target):
        li = self.counting_sort(li)
        new_li = []
        for i in range(len(li)):
            if li[i]==target:
                ind = li[i:].index(target) + len(li[:i])
                new_li.append(ind)
        return new_li