class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        res = [0] * n
        char_val = 1

        for i in range(n):
            if res[i] > 0:
                continue
            if char_val > 26:
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char_val
            char_val += 1

        word = "".join(chr(ord('a') + v - 1) for v in res)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                actual_lcp = 0
                if word[i] == word[j]:
                    actual_lcp = lcp[i + 1][j + 1] + 1 if i + 1 < n and j + 1 < n else 1

                if lcp[i][j] != actual_lcp:
                    return ""

        return word
