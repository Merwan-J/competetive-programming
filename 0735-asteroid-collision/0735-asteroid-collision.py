class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        
        
#         # cases
#         1 asteroids moving in diffrent direection
#             [-a,b]
#             a moving to the left  
#             b moving to the right
#             this is a case where they are moving in opposite direction but they won't be collided
#         2 asteroids moving in diffrenet direction
#             [a,-b]
#             a moving to the right 
#             b movint to the left
            
#             b will collide with a and explode
        
#         3 asteroids moving in the same direction 
#             [a,b] or [-a,-b]
#             they wont collide
        
#         [5,10]
        
#         [10]
        
#         [10,-5,-3]
#         []
        
        stack = []
        for num in nums:
            add = True
            while stack and stack[-1]>0 and num<0:
                if stack[-1]+num<0:
                    stack.pop()
                elif stack[-1] + num == 0:
                    stack.pop()
                    add = False
                    break
                else:
                    add = False
                    break
            
            if add:
                stack.append(num)
        
        return stack
    