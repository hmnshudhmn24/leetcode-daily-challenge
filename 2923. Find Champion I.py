class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for i, row in enumerate(grid):
            if sum(row) == len(grid) - 1:
                return i
        return -1
