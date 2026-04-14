from typing import List

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7
        masks = {}
        for i in range(2, 31):
            mask = 0
            temp = i
            valid = True
            for j, p in enumerate(primes):
                if temp % (p * p) == 0:
                    valid = False
                    break
                if temp % p == 0:
                    mask |= (1 << j)
            if valid: masks[i] = mask

        dp = [0] * (1 << 10)
        dp[0] = 1
        for x in nums:
            if x == 1:
                dp = [(v * 2) % mod for v in dp]
            elif x in masks:
                m = masks[x]
                for i in range((1 << 10) - 1, -1, -1):
                    if (i & m) == 0:
                        dp[i | m] = (dp[i | m] + dp[i]) % mod
        return (sum(dp) - 1) % mod
