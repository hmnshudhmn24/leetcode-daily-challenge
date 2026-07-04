from collections import deque, defaultdict
import sys

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))

        min_score = sys.maxsize
        visited = set()
        queue = deque([1])
        visited.add(1)

        while queue:
            node = queue.popleft()
            for neighbor, distance in adj[node]:
                min_score = min(min_score, distance)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return min_score
