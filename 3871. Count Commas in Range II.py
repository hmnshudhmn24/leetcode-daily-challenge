class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        limit = 1000
        while n >= limit:
            ans += n - limit + 1
            limit *= 1000
        return ans
