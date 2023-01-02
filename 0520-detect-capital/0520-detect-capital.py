class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        total = sum([char.isupper() for char in word])
        
        return (total==n) or (total==1 and word[0].isupper()) or (total==0)