class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = [[0] * len(matrix[0]) for i in range(len(matrix))]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        ans = 0
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            
            for dx, dy in dirs:
                new_i = i + dx
                new_j = j + dy

                if (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0])):
                    if matrix[new_i][new_j] > matrix[i][j]:
                        cache[i][j] = max(cache[i][j], 1 + dfs(new_i, new_j))
                
            return cache[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, 1 + dfs(i, j))
        return ans 


            

        