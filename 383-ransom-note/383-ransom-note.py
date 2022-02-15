class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = dict()
        for char in magazine:
            counter[char] = counter.get(char,0)+1
        
        for char in ransomNote:
            if char in counter and counter[char]>0:
                counter[char] -= 1
            else:
                return False
        return True