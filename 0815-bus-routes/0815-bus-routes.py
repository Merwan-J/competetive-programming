class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        G = defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                G[stop].append(i)
        
        Q = deque()
        Q.append([source,0])
        travelled_route = set()
        
        while Q:
            stop, buses_taken = Q.popleft()
            
            if stop == target:
                return buses_taken
            
            for bus in G[stop]:
                if bus not in travelled_route:
                    for s in routes[bus]:
                        Q.append([s, buses_taken+1])
                    travelled_route.add(bus)
                
        return -1