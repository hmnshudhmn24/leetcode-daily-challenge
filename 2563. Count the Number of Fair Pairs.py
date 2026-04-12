from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def countLess(target):
            res, l, r = 0, 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    res += (r - l)
                    l += 1
                else:
                    r -= 1
            return res
        return countLess(upper + 1) - countLess(lower)
