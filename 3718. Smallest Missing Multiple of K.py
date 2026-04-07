from typing import List

class Solution:
    def smallestMissingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        m = k
        while m in s:
            m += k
        return m
