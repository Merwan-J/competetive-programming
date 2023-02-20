class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(s): 
            arr = []
            cnt = 0
            lastChr = s[0]
            for c in s:
                if c == lastChr:
                    cnt += 1
                else:
                    arr.append((lastChr, cnt))
                    cnt = 1
                lastChr = c

            arr.append((lastChr, cnt))
            return arr

        def test(word, arrS):
            arrW = compress(word)
            if len(arrW) != len(arrS): return False  # mismatch number of groups
            for i in range(len(arrW)):
                if arrS[i][0] != arrW[i][0]: return False  # mismatch letter
                if not (arrS[i][1] == arrW[i][1] or arrS[i][1] >= max(3, arrW[i][1])):
                    return False
            return True

        arrS = compress(s)
        ans = 0
        for word in words:
            if test(word, arrS):
                ans += 1
        return ans