import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))
        busy = []
        res = [0] * k

        for i, (arr, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, s = heapq.heappop(busy)
                heapq.heappush(free, i + (s - i) % k)

            if free:
                s_idx = heapq.heappop(free)
                s = s_idx % k
                res[s] += 1
                heapq.heappush(busy, (arr + l, s))

        max_req = max(res)
        return [i for i, count in enumerate(res) if count == max_req]
