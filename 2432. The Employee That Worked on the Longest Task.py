class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        max_t = 0
        ans = float('inf')
        prev = 0
        for pid, t in logs:
            duration = t - prev
            if duration > max_t:
                max_t = duration
                ans = pid
            elif duration == max_t:
                ans = min(ans, pid)
            prev = t
        return ans
