class Solution:
    def maxOperations(self, li,k):
        li.sort()
        count = 0
        d = {}
        for i in li:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in li:
            if i > k:
                return count
            dif = k-i
            if dif in d:
                if dif == i and d[dif] >= 2:
                    d[dif] -= 2
                    count += 1
                if dif != i and d[dif] > 0 and d[i] > 0:
                    d[dif] -= 1
                    d[i] -= 1
                    count += 1
        return count


