from typing import List

class Solution:
    def computeAlternatingSum(self, nums: List[int]) -> int:
        return sum(nums[i] if i % 2 == 0 else -nums[i] for i in range(len(nums)))
