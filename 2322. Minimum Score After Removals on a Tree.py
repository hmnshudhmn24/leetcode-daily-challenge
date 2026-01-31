class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # DFS to setup subtree XORs and entry/exit times
        xor_subtree = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        def dfs(u, p):
            nonlocal timer
            timer += 1
            tin[u] = timer
            curr = nums[u]
            for v in adj[u]:
                if v != p:
                    curr ^= dfs(v, u)
            tout[u] = timer
            xor_subtree[u] = curr
            return curr

        dfs(0, -1)
        
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
            
        ans = float('inf')
        
        # Iterate all pairs of edges (represented by the child node of the edge)
        # We start from 1 because 0 is root and has no parent edge
        for i in range(1, n):
            for j in range(i + 1, n):
                # Calculate the 3 parts based on topology
                if is_ancestor(i, j): # i is above j
                    a = xor_subtree[j]
                    b = xor_subtree[i] ^ xor_subtree[j]
                    c = xor_subtree[0] ^ xor_subtree[i]
                elif is_ancestor(j, i): # j is above i
                    a = xor_subtree[i]
                    b = xor_subtree[j] ^ xor_subtree[i]
                    c = xor_subtree[0] ^ xor_subtree[j]
                else: # separate branches
                    a = xor_subtree[i]
                    b = xor_subtree[j]
                    c = xor_subtree[0] ^ xor_subtree[i] ^ xor_subtree[j]
                
                mx = max(a, b, c)
                mn = min(a, b, c)
                ans = min(ans, mx - mn)
                
        return ans
