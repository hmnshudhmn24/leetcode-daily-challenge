from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for u, v in allowedSwaps:
            union(u, v)

        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        res = 0
        for indices in components.values():
            count = Counter(source[i] for i in indices)
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1

        return res
