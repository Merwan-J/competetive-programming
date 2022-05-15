class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
#         [ 0, 1, 3, 5, 6]
            # 0, 1 ,2  3  4
                
#         [ 6, 5 , 3 , 1 , 0]
#           0  1   2   3   4
#         [ 10, 8, 5,  4,   3, 3, 2, 1, 1]
        
#           0   1  2    3   4  5  6  7  8
        
        daset = set(citations)
        if len(daset)==1:
            if (len(citations)==1 and citations[0]>=1) or (len(daset)==1 and citations[0]==1):
                return 1
            
        
        l,r = 0,len(citations)
        
        h = 0
        
        while l<=r and l<len(citations) and r>=0:
            mid = (l+r)//2  
                                                                                            
            if citations[mid]>=len(citations)-mid:
                h = len(citations)-mid
                r = mid - 1
            else:
                l = mid + 1
        
        return h
        
         