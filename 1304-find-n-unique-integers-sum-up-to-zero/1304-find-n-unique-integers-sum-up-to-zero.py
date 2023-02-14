class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        
        if n % 2 == 1:
            answer.append(0)
        
        for i in range(1, (n//2) + 1):
            answer.append(i)
            answer.append(-i)
            
        return answer