import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % 1000000007
