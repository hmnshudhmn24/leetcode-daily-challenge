class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]
