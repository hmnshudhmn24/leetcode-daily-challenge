from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        @cache
        def dfs(r, c, bal):
            if grid[r][c] == '(':
                bal += 1
            else:
                bal -= 1
            
            if bal < 0: return False
            if bal > (m + n) // 2: return False
            
            if r == m - 1 and c == n - 1:
                return bal == 0
            
            if r + 1 < m:
                if dfs(r + 1, c, bal): return True
            
            if c + 1 < n:
                if dfs(r, c + 1, bal): return True
                
            return False

        return dfs(0, 0, 0)
