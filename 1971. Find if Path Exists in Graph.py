from typing import List
import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
            
        # 1. Build adjacency list
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. Setup BFS
        queue = collections.deque([source])
        visited = set([source])
        
        # 3. Traverse
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
                
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False
