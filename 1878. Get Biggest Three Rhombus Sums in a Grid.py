from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                L = 1
                while i - L >= 0 and i + L < m and j - L >= 0 and j + L < n:
                    curr_sum = 0
                    r, c = i - L, j
                    while r < i:
                        curr_sum += grid[r][c]
                        r, c = r + 1, c + 1
                    while c > j:
                        curr_sum += grid[r][c]
                        r, c = r + 1, c - 1
                    while r > i:
                        curr_sum += grid[r][c]
                        r, c = r - 1, c - 1
                    while c < j:
                        curr_sum += grid[r][c]
                        r, c = r - 1, c + 1
                    sums.add(curr_sum)
                    L += 1
                    
        return sorted(list(sums), reverse=True)[:3]
