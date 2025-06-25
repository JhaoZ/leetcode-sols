class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dists = [[[0] * 2 for j in range(m)] for i in range(n)]
        visited = set()
        
        queue = deque()
        idx = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((idx, 0, i, j))
                    visited.add((idx, i, j))
                    idx += 1
        
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while queue:
            curr_id, curr_dist, curr_i, curr_j = queue.popleft()
            dists[curr_i][curr_j][0] += curr_dist
            dists[curr_i][curr_j][1] += 1
            for x, y in dirs:
                new_i = curr_i + x
                new_j = curr_j + y

                if 0 <= new_i < n and 0 <= new_j < m and ((curr_id, new_i, new_j) not in visited) and (grid[new_i][new_j] == 0):
                    visited.add((curr_id, new_i, new_j))
                    queue.append((curr_id, curr_dist + 1, new_i, new_j))
        
        house_dist = 2**31

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dists[i][j][1] == idx and dists[i][j][0] < house_dist:
                    house_dist = dists[i][j][0]

        return -1 if house_dist == 2**31 else house_dist
        