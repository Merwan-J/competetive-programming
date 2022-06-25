class Solution:
    # @return a string
    def minWindow(self, S, T):
        indices = {}
        for char in T:
            indices[char] = []
        miss = list(T)
        start = 0
        end = len(S)
        for i in range(len(S)):
            if S[i] in T:
                if S[i] not in miss and indices[S[i]] != []:
                    indices[S[i]].pop(0)
                elif S[i] in miss:
                    miss.remove(S[i])
                indices[S[i]].append(i)
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[0] for x in indices.values()])
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return S[start:end+1]