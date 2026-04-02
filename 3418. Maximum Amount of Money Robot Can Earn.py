class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][2] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for k in range(3):
                    mx_prev = -float('inf')
                    if i > 0:
                        mx_prev = max(mx_prev, dp[i - 1][j][k])
                    if j > 0:
                        mx_prev = max(mx_prev, dp[i][j - 1][k])

                    if mx_prev != -float('inf'):
                        dp[i][j][k] = mx_prev + coins[i][j]

                    if coins[i][j] < 0 and k < 2:
                        mx_prev_neut = -float('inf')
                        if i > 0:
                            mx_prev_neut = max(mx_prev_neut, dp[i - 1][j][k + 1])
                        if j > 0:
                            mx_prev_neut = max(mx_prev_neut, dp[i][j - 1][k + 1])

                        if mx_prev_neut != -float('inf'):
                            dp[i][j][k] = max(dp[i][j][k], mx_prev_neut)

        return max(dp[m - 1][n - 1])
