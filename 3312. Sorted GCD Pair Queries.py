import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1

        gcd_pairs = [0] * (max_num + 1)

        for i in range(max_num, 0, -1):
            c = sum(count[j] for j in range(i, max_num + 1, i))
            gcd_pairs[i] = c * (c - 1) // 2
            for j in range(2 * i, max_num + 1, i):
                gcd_pairs[i] -= gcd_pairs[j]

        prefix = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + gcd_pairs[i]

        return [bisect.bisect_right(prefix, q) for q in queries]
