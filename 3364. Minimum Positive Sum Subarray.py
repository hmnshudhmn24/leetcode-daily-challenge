from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = sum(nums[i:i + length])
                if s > 0:
                    min_sum = min(min_sum, s)
        return min_sum if min_sum != float('inf') else -1
