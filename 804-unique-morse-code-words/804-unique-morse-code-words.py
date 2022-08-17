class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse = {chr(i+ord('a')):code for i,code in enumerate(morse)}
        
        
        ans = set()
        
        for word in words:
            temp = []
            for char in word:
                temp.append(morse[char])
            ans.add(''.join(temp))
        
        return len(ans)