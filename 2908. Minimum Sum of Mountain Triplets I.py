class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        ans = min(ans, nums[i] + nums[j] + nums[k])
        return ans if ans != float('inf') else -1
