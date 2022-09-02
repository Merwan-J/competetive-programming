class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        
        
        for i,ingredients in enumerate(ingredients):
            indegree[recipes[i]]=len(ingredients)
            for ing in ingredients:
                outdegree[ing]+=[recipes[i]]
        
        q = deque(supplies)
        
        while q:
            ing = q.popleft()
            for recipe in outdegree[ing]:
                indegree[recipe]-=1
                if indegree[recipe]==0:
                    q.append(recipe)
        
        recipes = set(recipes)
        
        return [recipe for recipe in recipes if indegree[recipe]==0]