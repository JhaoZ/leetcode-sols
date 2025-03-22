class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        components = 0
        visited = set()

        def search(node, arr): 
            arr.append(node)           
            for n in graph[node]:
                if n in visited:
                    continue
                visited.add(n)
                search(n, arr)


        for i in range(n):
            if i in visited:
                continue
            curr_component = []
            visited.add(i)
            search(i, curr_component)

            print(curr_component)
            if len(curr_component) == 1:
                components += 1
                continue

            good = True
            for i in range(len(curr_component)):
                start = curr_component[i]
                for j in range(i + 1, len(curr_component)):
                    end = curr_component[j]
                    if not (start in graph[end] and end in graph[start]):
                        good = False
                        break
                if not good:
                    break
            if good:
                components += 1

        return components
            

            
            