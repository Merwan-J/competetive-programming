class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = {a: a for a in string.ascii_lowercase}
        
        def find(char):
            if parent[char] == char:
                return char
            parent[char] = find(parent[char])
            return parent[char]
        
        
        for eq in equations:
            if eq[1] == "=":
                parent[find(eq[-1])] = find(eq[0])
                
        
        parent = {a:find(parent[a]) for a in parent}
        
        for eq in equations:
            if eq[1] == "!" and find(eq[0]) == find(eq[-1]):
                return False
        
        return True
        
        
            
            
        
        
            