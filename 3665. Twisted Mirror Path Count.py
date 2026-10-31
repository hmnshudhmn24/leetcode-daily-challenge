class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 2 for _ in range(len(grid[0]) + 1)]
        dp[1] = [1] * 2

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    dp[c + 1] = [(dp[c + 1][1] + dp[c][0]) % MOD] * 2

        return dp[-1][0]
