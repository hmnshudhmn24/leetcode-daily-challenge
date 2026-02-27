from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = Counter(arr)
        freqs = sorted(counts.values(), reverse=True)
        removed = 0
        res = 0
        half = len(arr) // 2
        for f in freqs:
            removed += f
            res += 1
            if removed >= half:
                break
        return res
