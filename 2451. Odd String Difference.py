from collections import defaultdict

class Solution:
    def oddString(self, words: list[str]) -> str:
        d = defaultdict(list)
        for w in words:
            diff = tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1))
            d[diff].append(w)
        for k, v in d.items():
            if len(v) == 1:
                return v[0]
