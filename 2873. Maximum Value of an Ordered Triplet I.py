class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        res = 0
        max_diff = 0
        max_a = 0
        for num in nums:
            res = max(res, max_diff * num)
            max_diff = max(max_diff, max_a - num)
            max_a = max(max_a, num)
        return res
