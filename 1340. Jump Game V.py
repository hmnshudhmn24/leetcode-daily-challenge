from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            max_from_neighbors = 0

            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                max_from_neighbors = max(max_from_neighbors, dfs(j))

            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                max_from_neighbors = max(max_from_neighbors, dfs(j))

            dp[i] = 1 + max_from_neighbors
            return dp[i]

        return max(dfs(i) for i in range(n))
