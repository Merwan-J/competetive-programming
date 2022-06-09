class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        whole = set(supplies + recipes + [i for ing in ingredients for i in ing ])
        indegree = {i:set() for i in whole}
        outdegree = {i:set() for i in whole}
        zero = []
        
        for i in range(len(recipes)):
            rec = recipes[i]
            for ing in ingredients[i]:
                indegree[rec].add(ing)
                outdegree[ing].add(rec)
        
        for rec in supplies:
            if len(indegree[rec])==0:
                zero.append(rec)

        while zero:
            node = zero.pop()
            for adj in outdegree[node]:
                indegree[adj].remove(node)
                if len(indegree[adj])==0:
                    zero.append(adj)
        
        ans = []
        
        for rec,ing in indegree.items():
            if len(ing)==0 and rec in recipes:
                ans.append(rec)
        
        return ans
        
        