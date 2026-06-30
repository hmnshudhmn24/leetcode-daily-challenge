class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1, -1, -1]
        res = 0
        for i, char in enumerate(s):
            last_seen[ord(char) - ord('a')] = i
            res += min(last_seen) + 1
        return res
