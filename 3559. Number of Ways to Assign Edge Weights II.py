from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        if not edges:
            return [0] * len(queries)

        maxNode = 0
        for u, v in edges:
            maxNode = max(maxNode, u, v)

        n = maxNode + 1
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 20
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        visited = [False] * n

        startNode = 0
        for i in range(n):
            if adj[i]:
                startNode = i
                break

        q = deque([startNode])
        visited[startNode] = True

        while q:
            u = q.popleft()
            for i in range(1, LOG):
                up[u][i] = up[up[u][i - 1]][i - 1]

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    up[v][0] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        MOD = 1_000_000_007
        pow2 = [0] * (n + 1)
        pow2[0] = 1

        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        def getLca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]

            if u == v:
                return u

            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]

            return up[u][0]

        ans = [0] * len(queries)

        for i in range(len(queries)):
            u, v = queries[i]
            lca = getLca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]

            if dist > 0:
                ans[i] = pow2[dist - 1]
            else:
                ans[i] = 0

        return ans
