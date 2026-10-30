import heapq
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost > dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                new_cost = cost + w
                new_count = count + 1 if labels[u] == labels[v] else 1

                if new_count <= k:
                    if new_cost < dist[v][new_count]:
                        dist[v][new_count] = new_cost
                        heapq.heappush(pq, (new_cost, v, new_count))

        return -1
