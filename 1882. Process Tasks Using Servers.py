import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        res = []
        time = 0

        for i, t in enumerate(tasks):
            time = max(time, i)
            if not available:
                time = busy[0][0]
            while busy and busy[0][0] <= time:
                free_time, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))

            w, idx = heapq.heappop(available)
            res.append(idx)
            heapq.heappush(busy, (time + t, w, idx))

        return res
