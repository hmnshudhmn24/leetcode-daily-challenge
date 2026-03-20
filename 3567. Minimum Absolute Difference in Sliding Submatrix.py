class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        nums.append(grid[r][c])

                nums.sort()
                min_diff = float('inf')
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]:
                        min_diff = min(min_diff, nums[t] - nums[t - 1])

                ans[i][j] = min_diff if min_diff != float('inf') else 0

        return ans
