class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        i, j = nums.index(min(nums)), nums.index(max(nums))
        if i > j:
            i, j = j, i
        n = len(nums)
        return min(j + 1, n - i, i + 1 + n - j)
