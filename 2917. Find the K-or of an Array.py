class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(32):
            count = sum(1 for num in nums if (num >> i) & 1)
            if count >= k:
                ans |= (1 << i)
        return ans
