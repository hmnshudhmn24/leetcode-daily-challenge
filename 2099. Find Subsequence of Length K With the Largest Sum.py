class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        top_k_indices = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        return [nums[i] for i in sorted(top_k_indices)]
