from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Directions for moving Up, Down, Left, Right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Distance matrix to track min obstacles removed to reach (r, c)
        # Initialize with infinity
        min_obstacles = [[float('inf')] * n for _ in range(m)]
        min_obstacles[0][0] = 0

        # Deque for 0-1 BFS: Stores (row, col)
        queue = deque([(0, 0)])

        while queue:
            r, c = queue.popleft()

            # If we reached the target, return the cost immediately
            # Because 0-1 BFS guarantees we reach nodes in increasing order of cost
            if r == m - 1 and c == n - 1:
                return min_obstacles[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    new_dist = min_obstacles[r][c] + cost

                    # If we found a cheaper way to reach (nr, nc)
                    if new_dist < min_obstacles[nr][nc]:
                        min_obstacles[nr][nc] = new_dist

                        # CRITICAL: 0-cost moves go to FRONT, 1-cost moves go to BACK
                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))

        return -1 # Should not happen based on constraints
