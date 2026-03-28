class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collected = set()
        for i in range(len(nums) - 1, -1, -1):
            if 1 <= nums[i] <= k:
                collected.add(nums[i])
            if len(collected) == k:
                return len(nums) - i
        return -1
