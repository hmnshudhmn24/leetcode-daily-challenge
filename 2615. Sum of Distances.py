from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)

        ans = [0] * len(nums)

        for indices in indices_map.values():
            k = len(indices)
            if k == 1:
                continue

            current_sum = sum(indices) - k * indices[0]
            ans[indices[0]] = current_sum

            for m in range(k - 1):
                diff = indices[m+1] - indices[m]
                left_count = m + 1
                right_count = k - (m + 1)

                current_sum += (left_count - right_count) * diff
                ans[indices[m+1]] = current_sum

        return ans
