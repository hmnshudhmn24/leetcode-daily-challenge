from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {}
        for i in range(len(nums) - k + 1):
            for num in set(nums[i:i + k]):
                counts[num] = counts.get(num, 0) + 1

        ans = -1
        for num, freq in counts.items():
            if freq == 1 and num > ans:
                ans = num

        return ans
