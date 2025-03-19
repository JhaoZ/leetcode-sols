from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs_find(arr, curr_i, curr_j, visited):
            arr.append((curr_i, curr_j))
            for d in dirs:
                new_i, new_j = d[0] + curr_i, d[1] + curr_j
                if (new_i, new_j) not in visited and inBounds(new_i, new_j) and grid[new_i][new_j] == 1:
                    visited.add((new_i, new_j))
                    dfs_find(arr, new_i, new_j, visited)
        
        # Find first island
        island = []
        visited = set()
        foundNow = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    dfs_find(island, i, j, visited)
                    foundNow = True
                    break
            if foundNow:
                break

        def bfs(curr_i, curr_j):
            visited = set(island)  # Reset visited to include only the first island
            dist = {(curr_i, curr_j): 0}
            queue = deque()
            queue.append((curr_i, curr_j))
            while queue:
                curr = queue.popleft()
                tmp_i, tmp_j = curr
                for d in dirs:
                    new_i, new_j = tmp_i + d[0], tmp_j + d[1]
                    if (new_i, new_j) not in visited and inBounds(new_i, new_j):
                        visited.add((new_i, new_j))
                        dist[(new_i, new_j)] = dist[(tmp_i, tmp_j)] + 1
                        if grid[new_i][new_j] == 1:
                            return dist[(new_i, new_j)]
                        queue.append((new_i, new_j))
            return float('inf')
        
        ans = float('inf')
        for isl in island:
            ans = min(ans, bfs(isl[0], isl[1]))
        return ans - 1
