class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        run = defaultdict(int)
        palis = 0
        size = 0
        
        for word in words:
            rev = word[::-1]
            
            if run[rev]>0:
                size += 4
                run[rev]-=1
                palis = palis-1 if word == rev else palis
            else:
                run[word] += 1
                palis = palis + 1 if word == rev else palis
        
        size = size + 2 if palis else size
        
        return size
            