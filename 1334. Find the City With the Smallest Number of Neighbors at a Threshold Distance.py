class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        res = -1
        min_reachable = n
        for i in range(n):
            reachable = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable <= min_reachable:
                min_reachable = reachable
                res = i
        return res
