import math
import functools

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        @functools.lru_cache(None)
        def dp(i, g1, g2):
            if i == n:
                return 1 if (g1 > 0 and g1 == g2) else 0

            res = dp(i + 1, g1, g2)

            new_g1 = math.gcd(g1, nums[i]) if g1 > 0 else nums[i]
            res = (res + dp(i + 1, new_g1, g2)) % MOD

            new_g2 = math.gcd(g2, nums[i]) if g2 > 0 else nums[i]
            res = (res + dp(i + 1, g1, new_g2)) % MOD

            return res

        return dp(0, 0, 0)
