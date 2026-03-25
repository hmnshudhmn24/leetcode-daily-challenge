class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        total = sum(row_sums)
        if total % 2 != 0:
            return False

        target = total // 2

        curr = 0
        for i in range(m - 1):
            curr += row_sums[i]
            if curr == target:
                return True

        curr = 0
        for j in range(n - 1):
            curr += col_sums[j]
            if curr == target:
                return True

        return False
