from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 1. Check if Graph is Bipartite (2-colorable)
        # If not, return -1 immediately.
        colors = [0] * (n + 1)
        for i in range(1, n + 1):
            if colors[i] != 0: continue
            
            # BFS for Bipartite check
            q = deque([i])
            colors[i] = 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = -colors[u]
                        q.append(v)
                    elif colors[v] == colors[u]:
                        return -1 # Odd cycle detected
        
        # 2. Function to get max BFS depth starting from a specific node
        def get_bfs_depth(start_node):
            q = deque([(start_node, 1)]) # (node, depth)
            visited_bfs = {start_node}
            max_d = 1
            while q:
                u, d = q.popleft()
                max_d = d
                for v in adj[u]:
                    if v not in visited_bfs:
                        visited_bfs.add(v)
                        q.append((v, d + 1))
            return max_d

        # 3. Process each Connected Component
        visited_global = [False] * (n + 1)
        total_groups = 0
        
        for i in range(1, n + 1):
            if not visited_global[i]:
                # Identify all nodes in this component
                component_nodes = []
                q = deque([i])
                visited_global[i] = True
                component_nodes.append(i)
                
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if not visited_global[v]:
                            visited_global[v] = True
                            component_nodes.append(v)
                            q.append(v)
                
                # Find max groups possible for THIS component
                # We try starting BFS from every node in the component
                max_component_groups = 0
                for node in component_nodes:
                    max_component_groups = max(max_component_groups, get_bfs_depth(node))
                
                total_groups += max_component_groups
                
        return total_groups
