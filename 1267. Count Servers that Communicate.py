class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    ans += 1

        return ans
