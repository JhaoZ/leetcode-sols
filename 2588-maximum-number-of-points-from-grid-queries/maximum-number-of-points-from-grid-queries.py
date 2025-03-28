import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        num_queries = len(queries)
        sorted_queries = sorted((val, idx) for idx, val in enumerate(queries))
        results = [0] * num_queries
        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for query_value, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query_value:
                cell_value, x, y = heapq.heappop(min_heap)
                count += 1
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        heapq.heappush(min_heap, (grid[new_x][new_y], new_x, new_y))
            results[original_index] = count

        return results
