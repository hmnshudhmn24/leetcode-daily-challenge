from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            delta[a + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[b + limit + 1] += 1

        ans = n
        curr = n
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            if curr < ans:
                ans = curr

        return ans
