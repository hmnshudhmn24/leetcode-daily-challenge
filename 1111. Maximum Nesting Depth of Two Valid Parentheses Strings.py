from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return [i % 2 ^ (c == '(') for i, c in enumerate(seq)]
