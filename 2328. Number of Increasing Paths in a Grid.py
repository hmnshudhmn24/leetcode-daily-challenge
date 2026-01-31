class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        # Memoization cache
        memo = {}
        
        # Directions: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Each cell is a path of length 1 itself
            count = 1
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Check bounds and strictly increasing condition
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    count = (count + dfs(nr, nc)) % MOD
            
            memo[(r, c)] = count
            return count

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
                
        return ans
