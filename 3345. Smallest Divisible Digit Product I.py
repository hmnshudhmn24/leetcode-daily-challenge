class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(x):
            p = 1
            for d in str(x):
                p *= int(d)
            return p

        while prod(n) % t != 0:
            n += 1

        return n
