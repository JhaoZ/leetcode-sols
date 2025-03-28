class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        visited = set([])
        heap = [(grid[0][0], 0, 0)]
        sorted_queries = [(q, i) for i, q in enumerate(queries)]
        sorted_queries.sort()
        ans = [0] * len(queries)
        counter = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        for q, i in sorted_queries:
            if not heap:
                ans[i] = counter
                continue

            while heap and q > heap[0][0]:
                value, curr_x, curr_y = heapq.heappop(heap)
                
                if (curr_x, curr_y) in visited:
                    continue

                counter += 1
                visited.add((curr_x, curr_y))

                for x, y in dirs:
                    new_x, new_y = curr_x + x, curr_y + y

                    if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols:
                        continue
                    
                    heapq.heappush(heap, (grid[new_x][new_y], new_x, new_y))
            
            ans[i] = counter
        return ans


            
            


