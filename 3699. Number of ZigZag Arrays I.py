class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        dp0 = [1] * m
        dp1 = [1] * m

        for _ in range(1, n):
            next_dp0 = [0] * m
            next_dp1 = [0] * m

            sum0 = 0
            for j in range(m):
                next_dp1[j] = (next_dp1[j] + sum0) % MOD
                sum0 = (sum0 + dp0[j]) % MOD

            sum1 = 0
            for j in range(m - 1, -1, -1):
                next_dp0[j] = (next_dp0[j] + sum1) % MOD
                sum1 = (sum1 + dp1[j]) % MOD

            dp0 = next_dp0
            dp1 = next_dp1

        return (sum(dp0) + sum(dp1)) % MOD
