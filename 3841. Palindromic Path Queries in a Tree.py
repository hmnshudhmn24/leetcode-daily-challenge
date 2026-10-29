class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 16
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 1

        stack = [(0, -1)]
        while stack:
            u, p = stack.pop()
            if u >= 0:
                tin[u] = timer
                timer += 1
                up[u][0] = p if p != -1 else 0
                for i in range(1, LOG):
                    up[u][i] = up[up[u][i - 1]][i - 1]
                stack.append((~u, p))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u))
            else:
                u = ~u
                tout[u] = timer - 1

        bit = [0] * (n + 2)

        def add(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        chars = [ord(c) - 97 for c in s]
        for i in range(n):
            val = 1 << chars[i]
            add(tin[i], val)
            add(tout[i] + 1, val)

        def get_lca(u, v):
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

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = ord(parts[2]) - 97
                old_c = chars[u]
                if new_c != old_c:
                    val = (1 << old_c) ^ (1 << new_c)
                    add(tin[u], val)
                    add(tout[u] + 1, val)
                    chars[u] = new_c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = query(tin[u])
                mask_v = query(tin[v])
                mask_lca_char = 1 << chars[lca]
                path_mask = mask_u ^ mask_v ^ mask_lca_char
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans
