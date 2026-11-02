from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]

        moves = 0
        for x in nums:
            moves += abs(x - median)

        return moves
