class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            m = i
            for j in range(i + 1, n):
                total = prefix[j + 1] - prefix[i]

                while (prefix[m + 1] - prefix[i]) * 2 < total:
                    m += 1

                left_sum = prefix[m + 1] - prefix[i]
                res = 0

                if left_sum * 2 == total:
                    res = max(max_l[i][m], max_r[m + 1][j])
                else:
                    if m > i:
                        res = max(res, max_l[i][m - 1])
                    if m < j:
                        res = max(res, max_r[m + 1][j])

                dp[i][j] = res
                max_l[i][j] = max(max_l[i][j - 1], total + res)
                max_r[i][j] = max(max_r[i + 1][j], total + res)

        return dp[0][n - 1]
