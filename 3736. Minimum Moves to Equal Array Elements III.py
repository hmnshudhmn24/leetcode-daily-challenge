from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        moves = 0
        for n in nums:
            moves += max_val - n
        return moves
