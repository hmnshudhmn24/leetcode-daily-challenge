from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        return sum(nums) - mn * len(nums)
