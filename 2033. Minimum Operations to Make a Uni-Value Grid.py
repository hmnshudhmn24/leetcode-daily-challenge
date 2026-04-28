class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        nums = [val for row in grid for val in row]
        rem = nums[0] % x

        if any(val % x != rem for val in nums):
            return -1

        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(val - median) // x for val in nums)
