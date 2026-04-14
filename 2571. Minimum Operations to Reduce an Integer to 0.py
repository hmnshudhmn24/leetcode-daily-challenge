class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if (n & 3) == 3:
                n += 1
                res += 1
            else:
                res += (n & 1)
                n >>= 1
        return res
