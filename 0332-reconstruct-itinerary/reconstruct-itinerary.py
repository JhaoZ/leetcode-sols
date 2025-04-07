class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # src -> [dest, id]

        id_num = 0
        for src, dest in tickets:
            graph[src].append((dest, id_num))
            id_num += 1
        
        seen = set()
        path = []
        stack = ["JFK"]

        while len(stack) != 0:
            curr = stack[-1]
            next_hop, next_hop_id = None, None
            for dest, id_num in graph[curr]:
                if id_num in seen:
                    continue
                
                if next_hop is None:
                    next_hop = dest
                    next_hop_id = id_num
                else:
                    if dest < next_hop:
                        next_hop = dest
                        next_hop_id = id_num
            
            if next_hop is not None:
                seen.add(next_hop_id)
                stack.append(next_hop)
            else:
                stack.pop()
                path.append(curr)

        return path[::-1]


        