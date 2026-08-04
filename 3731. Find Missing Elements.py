from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)

        num_set = set(nums)

        missing = [i for i in range(min_num, max_num + 1) if i not in num_set]

        return missing
