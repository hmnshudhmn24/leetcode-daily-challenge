class Solution:
    def averageValue(self, nums: list[int]) -> int:
        valid = [x for x in nums if x % 6 == 0]
        return sum(valid) // len(valid) if valid else 0
