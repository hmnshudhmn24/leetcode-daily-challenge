from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        res = 0
        curr = 0
        for actual, minimum in tasks:
            if curr < minimum:
                res += minimum - curr
                curr = minimum
            curr -= actual
        return res
