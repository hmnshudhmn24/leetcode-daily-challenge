class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        return sum(1 for x in nums if x % 2 == 0) >= 2
