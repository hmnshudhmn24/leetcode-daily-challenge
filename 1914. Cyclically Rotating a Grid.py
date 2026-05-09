from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer

            vals = []

            for j in range(left, right):
                vals.append(grid[top][j])
            for i in range(top, bottom):
                vals.append(grid[i][right])
            for j in range(right, left, -1):
                vals.append(grid[bottom][j])
            for i in range(bottom, top, -1):
                vals.append(grid[i][left])

            eff_k = k % len(vals)
            vals = vals[eff_k:] + vals[:eff_k]

            idx = 0
            for j in range(left, right):
                grid[top][j] = vals[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = vals[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = vals[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = vals[idx]
                idx += 1

        return grid
