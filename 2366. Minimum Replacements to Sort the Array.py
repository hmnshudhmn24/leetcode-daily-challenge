from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[-1]
        operations = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                k = (nums[i] + prev - 1) // prev
                operations += (k - 1)
                prev = nums[i] // k
            else:
                prev = nums[i]

        return operations
