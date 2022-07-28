class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([i for i in sentence])) == 26