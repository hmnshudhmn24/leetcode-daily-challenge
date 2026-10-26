from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            stack = [(i, j)]
            total = 0
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] > 0:
                    visited[x][y] = True
                    total += grid[x][y]
                    stack.extend([
                        (x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1)
                    ])
            return total

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1

        return count
