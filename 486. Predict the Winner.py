class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}

        def get_score(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]

            pick_left = nums[i] - get_score(i + 1, j)
            pick_right = nums[j] - get_score(i, j - 1)

            res = max(pick_left, pick_right)
            memo[(i, j)] = res
            return res

        return get_score(0, len(nums) - 1) >= 0
