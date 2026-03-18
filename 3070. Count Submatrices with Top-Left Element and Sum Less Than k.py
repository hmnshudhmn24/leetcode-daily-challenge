class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                # 1. Calculate the 2D prefix sum in-place
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                if c > 0:
                    grid[r][c] += grid[r][c-1]
                if r > 0 and c > 0:
                    # Prevent double-counting the overlapping top-left region
                    grid[r][c] -= grid[r-1][c-1] 

                # 2. Check if the sum of the submatrix from (0,0) to (r,c) is <= k
                if grid[r][c] <= k:
                    count += 1

        return count
