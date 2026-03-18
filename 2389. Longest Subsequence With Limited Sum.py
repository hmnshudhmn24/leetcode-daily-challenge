from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return [bisect_right(nums, q) for q in queries]
