class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    res += 1
        return res
