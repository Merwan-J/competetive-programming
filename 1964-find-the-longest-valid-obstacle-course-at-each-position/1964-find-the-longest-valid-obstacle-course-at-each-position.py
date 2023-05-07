class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        """
        longest increasing subsequence ending at i for every i 
        
        
        
        
        [2, 3, 4, 1, 5]
        
        [1,2,]
        
        
        what is the min number so far
        what is the ordering of obstacles sofar (max_length, ending_index)
        
        [2,3,4,1,5]
        
        [5, 4, 3, 2, 1]
        
        """
        
        n = len(obstacles)
        answer = [1] * n
        
        lis = []
    
        for i, height in enumerate(obstacles):
            idx = bisect.bisect_right(lis, height)
            
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            answer[i] = idx + 1
            
        return answer