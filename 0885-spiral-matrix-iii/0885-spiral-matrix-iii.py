class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        answer = []
        
        def inBound(current_row, current_col):
            return -1<current_row<rows and -1<current_col<cols
        
        map_for_turns = {
            'U': 'R',
            'R': 'D',
            'D': 'L',
            'L': 'U'
        }
        
        current_row, current_col = rStart, cStart
        steps_allowed = 1
        current_direction = 'R'
        directions = {'U': [-1, 0],
                      'R': [0, 1],
                      'D': [1, 0],
                      'L': [0, -1]
                     }
        
        grid_size = rows*cols
        steps_taken = 0
        while len(answer) < grid_size:
            if inBound(current_row, current_col):
                answer.append([current_row, current_col])
            
            if steps_taken == steps_allowed:
                current_direction = map_for_turns[current_direction]
                steps_taken = 0
                
                if current_direction in ['L','R']:
                    steps_allowed += 1
            
            row_change, col_change = directions[current_direction]
            current_row += row_change
            current_col += col_change
            steps_taken += 1
 
        return answer
