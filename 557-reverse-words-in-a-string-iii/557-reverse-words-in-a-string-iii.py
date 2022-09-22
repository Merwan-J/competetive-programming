class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word[::-1] for word in s.split()]
        return " ".join(words)