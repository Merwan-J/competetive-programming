class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        
        what is the question asking?
            - check if I can reach the end of the array or not( last index )
        what are the values of the array represent?
            - the maximum jumps I can take from that given index
            - I can make a jump any index less or equal to the maximum jump jump
        
        line sweep??
        
        [2,3,1,1,4]
        [0,0,0,0,0]
        
        [1,0,0,-1,0]
        [1,1,0,-1,0]
        [1,1,1,-1,-1]
        [2,3,1,0,-1]
        
        [2,5,6,6,5]
        
        [3,2,1,0,4]
        [0,0,0,0,0]
        
        [1,0,0,0,-1]
        [1,1,0,0,-2]
        [1,1,1,0,-3]
        
        [1,2,3,3,0]
        
        
        [1,0,1,1,4]
        [0,0,0,0,0]
        
        [0,1,-1,0,0]
        [0,1,-1,0,0]
        [0,1,-1,1,-1]
        [0,1,-1,1,0]
        [0,1,0,1,1]
        
        [1,0,-1,0,0]
        [1,0,-1,0,0]
        [1,0,]
        
        """ 
#         n = len(nums)
#         sweep = [0]*n
#         sweep[0] = 1
        
#         for i in range(n-1):
#             jump = nums[i]
#             start = i+1
#             end = start+jump
            
#             sweep[start] += 1
#             if end<n:
#                 sweep[end] -= 1
        
#         psum = [0]
#         for i in range(1,n):
#             psum.append(psum[-1]+sweep[i])
        
#         return all(psum[1:])


        n = len(nums)
        prevJump = 1
        
        for i in range(n-1):
            curJump = nums[i]
            
            prevJump-=1
            prevJump = max(prevJump,curJump)
            
            if prevJump == 0:
                return False
        
        return True
        
        