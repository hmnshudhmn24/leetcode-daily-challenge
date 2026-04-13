from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, lookup = len(s), {}
        for i in range(n):
            if s[i] == '0':
                if 0 not in lookup: lookup[0] = [i, i]
                continue
            val = 0
            for j in range(i, min(i + 31, n)):
                val = (val << 1) | int(s[j])
                if val not in lookup: lookup[val] = [i, j]
        
        res = []
        for first, second in queries:
            target = first ^ second
            res.append(lookup.get(target, [-1, -1]))
        return res
