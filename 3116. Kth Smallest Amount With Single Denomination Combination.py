import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            if a == 0 or b == 0:
                return 0
            return abs(a * b) // gcd(a, b)

        lcm_cache = []
        for i in range(1, 1 << n):
            current_lcm = 1
            cnt = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_lcm = lcm(current_lcm, coins[j])
                    cnt += 1
            lcm_cache.append((current_lcm, cnt))

        def count(val):
            total = 0
            for l, cnt in lcm_cache:
                term = val // l
                if cnt % 2 == 1:
                    total += term
                else:
                    total -= term
            return total

        low, high = 1, min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
