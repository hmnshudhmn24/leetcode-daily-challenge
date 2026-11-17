import math

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        cost = [[math.inf] * (n + 1) for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n + 1):
                length = j - i
                sub = s[i:j]

                if length < 2:
                    continue

                min_ops_sub = math.inf

                for d in divisors[length]:
                    cur_ops = 0
                    for r in range(d):
                        l = r
                        r_ptr = length - 1 - (length - 1 - r) % d

                        while l < r_ptr:
                            if sub[l] != sub[r_ptr]:
                                cur_ops += 1
                            l += d
                            r_ptr -= d

                    if cur_ops < min_ops_sub:
                        min_ops_sub = cur_ops

                cost[i][j] = min_ops_sub

        dp = [cost[0][i] for i in range(n + 1)]

        for p in range(2, k + 1):
            new_dp = [math.inf] * (n + 1)

            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[j] != math.inf and cost[j][i] != math.inf:
                        if dp[j] + cost[j][i] < new_dp[i]:
                            new_dp[i] = dp[j] + cost[j][i]

            dp = new_dp

        return dp[n]
