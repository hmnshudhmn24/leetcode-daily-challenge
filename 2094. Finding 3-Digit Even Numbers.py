from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        counts = Counter(digits)
        res = []
        for i in range(100, 1000, 2):
            c = Counter(int(d) for d in str(i))
            if all(counts[k] >= v for k, v in c.items()):
                res.append(i)
        return res
