from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            count_target = 0

            for j in range(i, n):
                if nums[j] == target:
                    count_target += 1

                length = j - i + 1
                if count_target > length // 2:
                    result += 1

        return result
