import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Build the graph
        # graph[u] contains tuples of (neighbor, weight)
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            # Normal edge: u -> v with cost w
            graph[u].append((v, w))
            # Reversed edge (Switch): v -> u with cost 2*w
            graph[v].append((u, 2 * w))
        
        # Dijkstra's Algorithm
        # Priority Queue stores (current_cost, current_node)
        pq = [(0, 0)]
        
        # Distance array to track min cost to each node
        # Initialize with infinity
        min_costs = [float('inf')] * n
        min_costs[0] = 0
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
            # If we found a shorter path to u already, skip
            if current_cost > min_costs[u]:
                continue
            
            # If we reached the target
            if u == n - 1:
                return current_cost
            
            # Explore neighbors
            for v, weight in graph[u]:
                new_cost = current_cost + weight
                if new_cost < min_costs[v]:
                    min_costs[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        # If target is unreachable
        return -1
