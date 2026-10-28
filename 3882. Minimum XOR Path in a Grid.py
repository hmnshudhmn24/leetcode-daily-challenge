class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for j in range(1, n):
            dp[j] = {x ^ grid[0][j] for x in dp[j - 1]}

        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            new_dp[0] = {x ^ grid[i][0] for x in dp[0]}
            for j in range(1, n):
                new_dp[j] = {x ^ grid[i][j] for x in new_dp[j - 1] | dp[j]}
            dp = new_dp

        return min(dp[-1])
