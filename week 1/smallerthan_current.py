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
    def smallerNumbersThanCurrent(self,li):
        s = self.counting_sort(li)
        d = {}
        for i in set(s):
            d[i] = len(s[:s.index(i)])
        for i in range(len(li)):
            li[i] = d[li[i]]
        return li
        
