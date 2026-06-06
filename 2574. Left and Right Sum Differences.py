class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = 0
        res = []

        for num in nums:
            right_sum = total - left_sum - num
            res.append(abs(left_sum - right_sum))
            left_sum += num

        return res
