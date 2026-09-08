class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        base = 1000
        while n >= base:
            ans += n - base + 1
            base *= 1000
        return ans
