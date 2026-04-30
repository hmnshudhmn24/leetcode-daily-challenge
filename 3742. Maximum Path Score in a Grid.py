from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        k = min(k, m + n - 2)

        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cost = 1 if grid[i][j] > 0 else 0
                score = grid[i][j]

                prev_top = dp[j]
                new_dp_j = [-1] * (k + 1)

                if j > 0:
                    prev_left = dp[j - 1]
                    if cost == 0:
                        new_dp_j = [
                            v1 + score if v1 > v2 and v1 != -1 else
                            (v2 + score if v2 != -1 else -1)
                            for v1, v2 in zip(prev_top, prev_left)
                        ]
                    else:
                        new_dp_j[cost:] = [
                            v1 + score if v1 > v2 and v1 != -1 else
                            (v2 + score if v2 != -1 else -1)
                            for v1, v2 in zip(prev_top[:-cost], prev_left[:-cost])
                        ]
                else:
                    if cost == 0:
                        new_dp_j = [v + score if v != -1 else -1 for v in prev_top]
                    else:
                        new_dp_j[cost:] = [v + score if v != -1 else -1 for v in prev_top[:-cost]]

                dp[j] = new_dp_j

        return max(dp[-1])
