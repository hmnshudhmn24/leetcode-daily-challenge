from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        res = 1
        while res in s:
            res <<= 1
        return res
