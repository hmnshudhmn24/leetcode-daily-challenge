import math
import heapq

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0

        LOG = n.bit_length()

        st_max = [[0] * LOG for _ in range(n)]
        st_min = [[0] * LOG for _ in range(n)]

        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])

        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1

        def get_score(L, R):
            if L > R:
                return 0
            length = R - L + 1
            j = log_table[length]
            max_val = max(st_max[L][j], st_max[R - (1 << j) + 1][j])
            min_val = min(st_min[L][j], st_min[R - (1 << j) + 1][j])
            return max_val - min_val

        pq = []
        for i in range(n):
            heapq.heappush(pq, (-get_score(i, n - 1), i, n - 1))

        ans = 0
        for _ in range(k):
            if not pq:
                break
            neg_score, L, R = heapq.heappop(pq)
            ans -= neg_score

            if R > L:
                heapq.heappush(pq, (-get_score(L, R - 1), L, R - 1))

        return ans
