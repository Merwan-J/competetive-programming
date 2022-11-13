class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        
        return " ".join(reversed(s))