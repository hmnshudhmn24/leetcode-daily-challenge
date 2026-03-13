import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        l = 1
        r = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = r
        
        while l <= r:
            m = (l + r) // 2
            s = sum((math.isqrt(1 + 8 * m // t) - 1) // 2 for t in workerTimes)
            if s >= mountainHeight:
                ans = m
                r = m - 1
            else:
                l = m + 1
                
        return ans
