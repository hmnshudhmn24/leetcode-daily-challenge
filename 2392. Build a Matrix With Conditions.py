from typing import List
from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # Helper function to perform Topological Sort
        def topological_sort(conditions, n):
            graph = defaultdict(list)
            indegree = {i: 0 for i in range(1, n + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            queue = deque([node for node in indegree if indegree[node] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            # If we couldn't process all nodes, there is a cycle
            if len(order) < n:
                return []
            return order

        # 1. Get the order for rows and columns
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        # If either contains a cycle, return empty
        if not row_order or not col_order:
            return []
            
        # 2. Map values to their specific indices
        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: i for i, val in enumerate(col_order)}
        
        # 3. Construct the matrix
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            r, c = row_pos[num], col_pos[num]
            matrix[r][c] = num
            
        return matrix
