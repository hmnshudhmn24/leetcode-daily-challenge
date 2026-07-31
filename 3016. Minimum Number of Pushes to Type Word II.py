from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(count * ((i // 8) + 1) for i, count in enumerate(sorted(Counter(word).values(), reverse=True)))
