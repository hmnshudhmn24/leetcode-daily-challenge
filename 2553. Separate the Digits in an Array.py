class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            for digit in str(num):
                res.append(int(digit))
        return res
