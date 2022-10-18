class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        stringLen = len(s)
        effect = [0]*stringLen
        
        for i,num in enumerate(shifts):
            effect[0] += num
            
            if i+1 < stringLen:
                effect[i+1]-=num
        
        prefixSum = [effect[0]]
        
        for i in range(1,stringLen):
            prefixSum.append(effect[i]+prefixSum[-1])
        
        answer = []
        
        for i,shift in enumerate(prefixSum):
            char_ord = (ord(s[i])-ord('a') + shift)%26 + ord('a')
            answer.append(chr(char_ord))
        return "".join(answer)