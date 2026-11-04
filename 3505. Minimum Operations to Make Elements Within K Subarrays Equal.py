import heapq


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        min_ops = []
        lower = []
        upper = []
        lower_sum = 0
        upper_sum = 0
        lower_size = 0
        upper_size = 0
        deleted_lower = {}
        deleted_upper = {}

        for i in range(n):
            num = nums[i]
            if lower_size == 0 or num <= -lower[0]:
                heapq.heappush(lower, -num)
                lower_sum += num
                lower_size += 1
            else:
                heapq.heappush(upper, num)
                upper_sum += num
                upper_size += 1

            if i >= x:
                out = nums[i - x]
                if out <= -lower[0]:
                    deleted_lower[out] = deleted_lower.get(out, 0) + 1
                    lower_sum -= out
                    lower_size -= 1
                else:
                    deleted_upper[out] = deleted_upper.get(out, 0) + 1
                    upper_sum -= out
                    upper_size -= 1

            while lower_size > upper_size + 1:
                while lower and deleted_lower.get(-lower[0], 0) > 0:
                    deleted_lower[-lower[0]] -= 1
                    heapq.heappop(lower)
                val = -heapq.heappop(lower)
                lower_sum -= val
                lower_size -= 1
                heapq.heappush(upper, val)
                upper_sum += val
                upper_size += 1

            while upper_size > lower_size:
                while upper and deleted_upper.get(upper[0], 0) > 0:
                    deleted_upper[upper[0]] -= 1
                    heapq.heappop(upper)
                val = heapq.heappop(upper)
                upper_sum -= val
                upper_size -= 1
                heapq.heappush(lower, -val)
                lower_sum += val
                lower_size += 1

            while lower and deleted_lower.get(-lower[0], 0) > 0:
                deleted_lower[-lower[0]] -= 1
                heapq.heappop(lower)
            while upper and deleted_upper.get(upper[0], 0) > 0:
                deleted_upper[upper[0]] -= 1
                heapq.heappop(upper)

            if i >= x - 1:
                median = -lower[0]
                cost = (median * lower_size - lower_sum) + (upper_sum - median * upper_size)
                min_ops.append(cost)

        m = len(min_ops)
        dp = [[float('inf')] * (k + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, k + 1):
                skip = dp[i + 1][j]
                if i + x <= m:
                    take = min_ops[i] + dp[i + x][j - 1]
                else:
                    take = min_ops[i] if j == 1 else float('inf')
                dp[i][j] = min(skip, take)

        return int(dp[0][k])
