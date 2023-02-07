
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        clockwise = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        anti_clockwise = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

        x, y = (0, 0)
        direction = 'N'
        
        for _ in range(4):
            for s in instructions:
                if s == 'L':
                    direction = anti_clockwise[direction]
                elif s == 'R':
                    direction = clockwise[direction]
                elif s == 'G':
                    if direction == 'N':
                        y+=1
                    elif direction == 'S':
                        y-=1
                    elif direction == 'E':
                        x+=1
                    elif direction == 'W':
                        x-=1

            if x == 0 and y == 0:
                return True
        return False