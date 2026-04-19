class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        stack = []
        to_remove = len(nums) - k
        for num in nums:
            while stack and stack[-1] > num and to_remove > 0:
                stack.pop()
                to_remove -= 1
            stack.append(num)
        return stack[:k]
