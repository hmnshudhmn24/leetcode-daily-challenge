from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        buckets = defaultdict(list)
        for i, val in enumerate(nums):
            x = val
            while x > 1:
                p = spf[x]
                buckets[p].append(i)
                while x % p == 0:
                    x //= p

        queue = deque([(0, 0)])
        seen = {0}

        while queue:
            curr, steps = queue.popleft()
            if curr == n - 1:
                return steps

            for nxt in (curr - 1, curr + 1):
                if 0 <= nxt < n and nxt not in seen:
                    if nxt == n - 1:
                        return steps + 1
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))

            val = nums[curr]
            if val >= 2 and spf[val] == val:
                if val in buckets:
                    for nxt in buckets[val]:
                        if nxt not in seen:
                            if nxt == n - 1:
                                return steps + 1
                            seen.add(nxt)
                            queue.append((nxt, steps + 1))
                    del buckets[val]

        return -1
