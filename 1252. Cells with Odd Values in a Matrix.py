from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_counts = [0] * m
        col_counts = [0] * n

        for r, c in indices:
            row_counts[r] ^= 1
            col_counts[c] ^= 1

        odd_rows = sum(row_counts)
        odd_cols = sum(col_counts)

        return odd_rows * (n - odd_cols) + odd_cols * (m - odd_rows)
