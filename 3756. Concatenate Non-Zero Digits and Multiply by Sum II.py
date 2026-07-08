from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        p = [0] * (n + 1)
        cnt = [0] * (n + 1)
        total_sum = [0] * (n + 1)

        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % mod
            d = int(s[i])
            total_sum[i + 1] = total_sum[i] + d
            if d > 0:
                cnt[i + 1] = cnt[i] + 1
                p[i + 1] = (p[i] * 10 + d) % mod
            else:
                cnt[i + 1] = cnt[i]
                p[i + 1] = p[i]

        ans = [0] * len(queries)
        for i in range(len(queries)):
            l, r = queries[i]
            c = cnt[r + 1] - cnt[l]
            s_val = total_sum[r + 1] - total_sum[l]
            val = (p[r + 1] - p[l] * pow10[c]) % mod
            ans[i] = (val * s_val) % mod

        return ans
