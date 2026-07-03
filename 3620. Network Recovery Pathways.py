from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        max_w = -1

        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                indeg[v] += 1
                if w > max_w:
                    max_w = w

        q = [i for i in range(n) if indeg[i] == 0]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v, w in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(mid: int) -> bool:
            dist = [float("inf")] * n
            dist[0] = 0
            for u in q:
                if dist[u] != float("inf"):
                    for v, w in g[u]:
                        if w >= mid and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w
            return dist[n - 1] <= k

        l, r = 0, max_w
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
