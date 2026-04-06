class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = [ord(c) - ord('a') + 1 for c in s]
        l = 0
        r = sum(scores)
        for i in range(len(s) - 1):
            l += scores[i]
            r -= scores[i]
            if l == r:
                return True
        return False
