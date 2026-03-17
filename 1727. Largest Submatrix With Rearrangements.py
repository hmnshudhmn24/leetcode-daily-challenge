class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != 0 and r > 0:
                    matrix[r][c] += matrix[r-1][c]

            curr_row = sorted(matrix[r], reverse=True)

            for i in range(cols):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans
