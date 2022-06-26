class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        psum = [0]
        for i in cardPoints:
            psum.append(psum[-1]+i)
        
        l,r = 0,len(cardPoints)-k
        ans = 0
        
        while r<len(psum):
            ans = max(ans,psum[-1]-(psum[r]-psum[l]))
            l+=1
            r+=1
        
        return ans