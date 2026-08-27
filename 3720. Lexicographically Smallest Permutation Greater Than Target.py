from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        matched_len = 0

        while matched_len < n and count[target[matched_len]] > 0:
            count[target[matched_len]] -= 1
            matched_len += 1

        for k in range(matched_len, -1, -1):
            if k < n:
                for char_code in range(ord(target[k]) + 1, 123):
                    char = chr(char_code)
                    if count[char] > 0:
                        count[char] -= 1
                        res = target[:k] + char
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            if count[c] > 0:
                                res += c * count[c]
                        return res
            if k > 0:
                count[target[k - 1]] += 1

        return ""
