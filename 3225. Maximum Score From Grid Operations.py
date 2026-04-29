class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        col_sum = [[0] * (n + 1) for _ in range(n)]

        for j in range(n):
            for i in range(n):
                col_sum[j][i + 1] = col_sum[j][i] + grid[i][j]

        memo = [[[-1] * 2 for _ in range(n + 1)] for _ in range(n)]

        def dfs(j: int, pre: int, dec: int) -> int:
            if j < 0:
                return 0
            if memo[j][pre][dec] != -1:
                return memo[j][pre][dec]

            res = 0
            for cur in range(n + 1):
                if pre == cur:
                    res = max(res, dfs(j - 1, cur, 0))
                elif pre > cur:
                    res = max(res, dfs(j - 1, cur, 1) + col_sum[j][pre] - col_sum[j][cur])
                elif dec:
                    if pre == 0:
                        res = max(res, dfs(j - 1, cur, 0))
                else:
                    res = max(res, dfs(j - 1, cur, 0) + col_sum[j + 1][cur] - col_sum[j + 1][pre])

            memo[j][pre][dec] = res
            return res

        return max(dfs(n - 2, i, 0) for i in range(n + 1))
