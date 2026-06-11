from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0
        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

        if max_depth == 0:
            return 0

        return pow(2, max_depth - 1, 10**9 + 7)
