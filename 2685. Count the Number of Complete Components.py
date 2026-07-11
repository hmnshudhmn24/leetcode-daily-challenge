class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        res = 0

        for i in range(n):
            if i not in visited:
                queue = [i]
                visited.add(i)
                component_nodes = []

                while queue:
                    curr = queue.pop(0)
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                v_count = len(component_nodes)
                e_count = sum(len(adj[node]) for node in component_nodes) // 2

                if e_count == v_count * (v_count - 1) // 2:
                    res += 1

        return res
