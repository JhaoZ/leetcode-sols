class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)
        endPoints = []
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        for a, val in graph.items():
            if len(val) == 1:
                endPoints.append(a)
        
        visited = set()
        def dfs(curr):
            
            ans.append(curr)
            for node in graph[curr]:
                if node in visited:
                    continue
                visited.add(node)
                dfs(node)

        visited.add(endPoints[0])
        dfs(endPoints[0])

        return ans
        


        

        