class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        def find(parent, x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(parent, rank, x, y):
            px, py = find(parent, x), find(parent, y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        must_edges = [(u, v, s) for u, v, s, m in edges if m == 1]
        opt_edges  = [(u, v, s) for u, v, s, m in edges if m == 0]
        
        # Check: must edges form a cycle → impossible
        parent = list(range(n))
        rank   = [0] * n
        for u, v, s in must_edges:
            if not union(parent, rank, u, v):
                return -1
        
        # Check: overall connectivity (must + all optional)
        parent2 = list(range(n))
        rank2   = [0] * n
        for u, v, s in must_edges:
            union(parent2, rank2, u, v)
        for u, v, s in opt_edges:
            union(parent2, rank2, u, v)
        root = find(parent2, 0)
        if any(find(parent2, i) != root for i in range(1, n)):
            return -1
        
        def feasible(mid: int) -> bool:
            par = list(range(n))
            rnk = [0] * n
            
            # Must-include edges
            for u, v, s in must_edges:
                if s < mid:
                    return False
                union(par, rnk, u, v)
            
            # Optional edges that need NO upgrade (s >= mid)
            for u, v, s in opt_edges:
                if s >= mid:
                    union(par, rnk, u, v)
            
            # Optional edges that need ONE upgrade (s < mid but 2s >= mid)
            upgrades_used = 0
            for u, v, s in opt_edges:
                if s < mid <= 2 * s:
                    if find(par, u) != find(par, v):
                        union(par, rnk, u, v)
                        upgrades_used += 1
                        if upgrades_used > k:
                            return False
            
            # All nodes must be connected
            root = find(par, 0)
            return all(find(par, i) == root for i in range(1, n))
        
        lo, hi, ans = 1, 2 * 10**5, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo  = mid + 1
            else:
                hi  = mid - 1
        
        return ans
