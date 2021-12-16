class Solution:
    def kthLargestNumber(self, li: List[str], k: int) -> str:
        li =  [int(i) for i in li]
        return str(sorted(li)[::-1][k-1])
                
        