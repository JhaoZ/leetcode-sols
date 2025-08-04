class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        temp = [ch for ch in s]
        components = []

        graph = defaultdict(list)
        nodes = set()
        for start, end in pairs:
            graph[start].append(end)
            graph[end].append(start)
            nodes.add(start)
            nodes.add(end)
        
        visited = set()

        def dfs(curr, arr):
            arr.append((temp[curr], curr))
            for n in graph[curr]:
                if n in visited:
                    continue
                visited.add(n)
                dfs(n, arr)

        for n in nodes:
            if n in visited:
                continue
            visited.add(n)
            arr = []
            dfs(n, arr)
            components.append(arr)

        for c in components:
            indexes = sorted([idx for _, idx in c])
            chars = sorted([ch for ch, _ in c])
            


            for ch, idx in zip(chars, indexes):
                temp[idx] = ch
        
        return "".join(temp)

        

