import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = math.gcd(a, b)
        return sum(1 for i in range(1, g + 1) if g % i == 0)
