class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(curr, arr):
            if curr == len(graph) - 1:
                ans.append(arr[:])
                return

            for n in graph[curr]:
                arr.append(n)
                dfs(n, arr)
                arr.pop()
        
        dfs(0, [0])
        return ans
        
        