class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = set()
        l = []
        d = {}
        if trust == [] and n==1:
            return 1
        for i in trust:
            s.add(i[0])
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]] += 1

        for i in d:
            if d[i] == n-1 and i not in s:
                l.append(i)

        return l[0] if len(l) == 1 else -1

         
