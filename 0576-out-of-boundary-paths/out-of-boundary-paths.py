class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        @cache
        def dp(i, j, move):
            if move >= 0:
                if i < 0 or j < 0 or i >= m or j >= n:
                    return 1
            else:
                return 0
            
            curr = 0
            for di, dj in dirs:
                curr = (curr + dp(i + di, j + dj, move - 1)) % (10**9+7)
            return curr

        return dp(startRow, startColumn, maxMove)
        