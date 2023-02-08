class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

        start = adjacentPairs[0][0]
        for k, v in adj.items():
            if len(v) ==1:
                start = k
                break
				
        nums=[]
        seen = set()
        def dfs(num):
            seen.add(num)
            for next_num in adj[num]:
                if next_num in seen: continue
                dfs(next_num)
            nums.append(num) 
        dfs(start)
        return nums