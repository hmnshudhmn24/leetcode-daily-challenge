class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        z = [len(p) for p in s.split('1') if p]
        if len(z) < 2:
            return s.count('1')
        return s.count('1') + max(z[i] + z[i + 1] for i in range(len(z) - 1))
