class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = [0]
        opened = [False]*n
        
        while keys:
            cur = keys.pop()
            opened[cur] = True
            
            for room in rooms[cur]:
                if not opened[room]:
                    keys.append(room)
                    
        return sum(opened) == n