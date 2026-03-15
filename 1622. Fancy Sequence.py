class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.vals = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        # We need to store v such that: (v * mul + add) % MOD = val
        # Therefore: v = (val - add) * inverse(mul)
        val = (val - self.add) % self.MOD
        # Python's pow(a, b, m) computes (a^b) % m efficiently
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        self.vals.append((val * inv_mul) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.vals[idx] * self.mul + self.add) % self.MOD
