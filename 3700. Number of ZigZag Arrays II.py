class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        k = r - l + 1

        def mul(A, B):
            return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*B)] for row in A]

        T = [[1 if j >= k - i else 0 for j in range(k)] for i in range(k)]
        res = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
        p = n - 2
        base = T

        while p > 0:
            if p % 2 == 1:
                res = mul(res, base)
            base = mul(base, base)
            p //= 2

        ans = 0
        V = list(range(k))

        for i in range(k):
            val = sum(res[i][j] * V[j] for j in range(k)) % mod
            ans = (ans + val) % mod

        return (ans * 2) % mod
