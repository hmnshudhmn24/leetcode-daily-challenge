from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        drop_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop_count += 1

        return drop_count <= 1
