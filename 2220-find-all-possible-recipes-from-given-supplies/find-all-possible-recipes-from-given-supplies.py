class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe = {}
        for i in range(len(recipes)):
            recipe[recipes[i]] = ingredients[i]

        cache = {}
        visited = set()
        supply = set(supplies)
        for s in supply:
            cache[s] = True
        
        def check(r):
            if r in cache:
                return cache[r]
            
            if r not in recipe or r in visited:
                return False
            
            visited.add(r)

            canMake = True
            for i in recipe[r]:
                if check(i) == False:
                    canMake = False
            
            cache[r] = canMake
            return canMake

        ans = []
        for r in recipes:
            if check(r):
                ans.append(r)
        return ans

        