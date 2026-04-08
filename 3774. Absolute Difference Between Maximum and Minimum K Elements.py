from typing import List

class Solution:
    def absoluteDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[-k:]) - sum(nums[:k]))
