class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        s = set(nums)
        ans = -1
        for x in nums:
            if x > 0 and -x in s:
                ans = max(ans, x)
        return ans
