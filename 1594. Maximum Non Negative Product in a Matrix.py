class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]

        mx[0][0] = mn[0][0] = grid[0][0]

        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i-1][0] * grid[i][0]
        for j in range(1, n):
            mx[0][j] = mn[0][j] = mx[0][j-1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                p1 = mx[i-1][j] * grid[i][j]
                p2 = mx[i][j-1] * grid[i][j]
                p3 = mn[i-1][j] * grid[i][j]
                p4 = mn[i][j-1] * grid[i][j]

                mx[i][j] = max(p1, p2, p3, p4)
                mn[i][j] = min(p1, p2, p3, p4)

        if mx[-1][-1] < 0:
            return -1

        return mx[-1][-1] % (10**9 + 7)
