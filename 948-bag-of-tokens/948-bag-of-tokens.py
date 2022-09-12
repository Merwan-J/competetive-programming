class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score,ans = 0,0
        l,r = 0,len(tokens)-1
        
        while l<=r:
            cur = tokens[l]
            if cur>power and score ==0:
                break
            elif cur>power and score >0:
                power += tokens[r]
                r-=1
                score-=1
            else:
                power-=cur
                l+=1
                score+=1
            ans = max(ans,score)
        return ans
        