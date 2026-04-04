class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        seen = set()
        repeated = -1
        for row in grid:
            for val in row:
                if val in seen:
                    repeated = val
                seen.add(val)
        missing = -1
        for i in range(1, n * n + 1):
            if i not in seen:
                missing = i
                break
        return [repeated, missing]
