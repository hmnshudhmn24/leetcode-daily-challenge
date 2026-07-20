class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        if k == 0:
            return grid

        flat = [grid[i][j] for i in range(m) for j in range(n)]
        flat = flat[-k:] + flat[:-k]

        return [[flat[i * n + j] for j in range(n)] for i in range(m)]
