from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        return sum(num * count for num, count in freq.items() if count % k == 0)
