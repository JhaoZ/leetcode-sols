class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
        flatten.sort()
        i, j = 0, len(flatten) - 1
        minima = min(flatten)
        ops = 0
        while i <= j :
            if abs(flatten[i] - minima) % x != 0 or abs(flatten[j] - minima) % x != 0 :
                return -1
            ops += abs(flatten[i] - flatten[j]) // x
            i += 1
            j -= 1
        return ops

