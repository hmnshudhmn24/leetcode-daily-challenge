from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        f = [float('inf')] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in range(max(0, i - 3), i):
                f[i] = min(f[i], f[j] + costs[i - 1] + (i - j) ** 2)
        return f[n]
