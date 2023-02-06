class Solution:
    def racecar(self, target: int) -> int:
        memory = {}
        queue = deque([(0, 1)])
        step = 0    
        
        while queue:
            lens = len(queue)
            i = 0 
            
            while i < lens:
                position, speed = queue.popleft()
                if memory.get((position, speed)) or (abs(position) > 2 * target):
                    i += 1
                    continue
                    
                memory[(position, speed)] = True
                if position == target:
                    return step
                
                queue.append((position+speed, speed * 2))
                
                if speed > 0:
                    queue.append((position, -1))
                else:
                    queue.append((position, 1))
                    
                i += 1
            step += 1
            
        return 0