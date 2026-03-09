class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        row_strengths = [(sum(row), i) for i, row in enumerate(mat)]
        row_strengths.sort()
        return [i for _, i in row_strengths[:k]]
