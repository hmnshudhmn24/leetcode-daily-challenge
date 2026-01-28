class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # dp[t][i][j] initialized to infinity
        dp = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        
        # Base case
        dp[0][0][0] = 0
        
        # Precompute groups of coordinates for each value
        groups = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in groups:
                    groups[val] = []
                groups[val].append((r, c))
        
        # Sort unique values descending for efficient teleport handling
        sorted_vals = sorted(groups.keys(), reverse=True)
        
        for t in range(k + 1):
            # 1. Normal Moves Propagation (Current Layer)
            for r in range(m):
                for c in range(n):
                    cost = grid[r][c]
                    if r > 0:
                        dp[t][r][c] = min(dp[t][r][c], dp[t][r-1][c] + cost)
                    if c > 0:
                        dp[t][r][c] = min(dp[t][r][c], dp[t][r][c-1] + cost)
            
            # 2. Teleport Moves (Prepare Next Layer)
            if t < k:
                min_source_cost = float('inf')
                for val in sorted_vals:
                    # Collect sources: Cells with value >= val (processed so far) 
                    # can be jump-off points.
                    # We add current group's costs to the pool of valid sources.
                    for r, c in groups[val]:
                        min_source_cost = min(min_source_cost, dp[t][r][c])
                    
                    # Apply to destinations: Cells with value == val can be reached
                    # from any source with value >= val.
                    for r, c in groups[val]:
                        dp[t+1][r][c] = min(dp[t+1][r][c], min_source_cost)

        # Result is min cost to reach bottom-right across all k layers
        ans = float('inf')
        for t in range(k + 1):
            ans = min(ans, dp[t][m-1][n-1])
            
        return ans
