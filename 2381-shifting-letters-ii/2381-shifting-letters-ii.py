class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        stringLen = len(s)
        effect = [0]*stringLen
        
        for start,end,direction in shifts:
            shift = 1 if direction == 1 else -1
            effect[start]+=shift

#           to curb the above above effect
            if end+1<stringLen:
                effect[end+1]-=shift
        
        prefixSum = [effect[0]]
        for i in range(1,stringLen):
            prefixSum.append(prefixSum[-1]+effect[i])
        
        # print(prefixSum)
        
        answer = []
        
        for i,char in enumerate(s):
            char_ord = ord(char)-ord('a')
            new_char_ord = ((char_ord + prefixSum[i])%26) + ord('a')
            answer.append(chr(new_char_ord))
        return "".join(answer)