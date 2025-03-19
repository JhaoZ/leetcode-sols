class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if (obstacleGrid[0][0] == 1):
            return 0

        @cache
        def dp(i, j):
            
            if i == n - 1 and j == m - 1:
                return 1
            
            ans = 0
            if 0 <= i + 1 < n and obstacleGrid[i + 1][j] == 0:
                ans += dp(i + 1, j)

            if 0 <= j + 1 < m and obstacleGrid[i][j + 1] == 0:
                ans += dp(i, j + 1)
            return ans
        return dp(0,0)