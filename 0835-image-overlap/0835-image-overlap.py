class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n=len(A)
        pts1=[(i,j) for i in range(n) for j in range(n) if A[i][j]==1]
        pts2=[(i,j) for i in range(n) for j in range(n) if B[i][j]==1]
        counter = collections.Counter((x1-x2,y1-y2) for x1,y1 in pts1 for x2,y2 in pts2)
        return max(counter.values() or [0])
        